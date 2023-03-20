## poems.rpy

# This file defines all the poems in the game that can be shown to the player
# by the girls in the poem sharing mini-game.

init 1 python:

    class Author(object):
        """
        A class used to default values of a `Poem` instance.

        `name`: str
            The auhtor's name
        
        See the `Poem` class for more information.
        """

        def __init__(self, name, style=True, paper="images/bg/poem.jpg", separate_title_from_text=True, music=None):
            self.name = name
            self.style = style
            self.paper = paper
            self.separate_title_from_text = separate_title_from_text
            self.music = music
    
    author_s = Author("sayori", music=audio.tsayori)
    author_m = Author("monika", music=audio.tmonika)
    author_n = Author("natsuki", music=audio.tnatsuki)
    author_y = Author("yuri", music=audio.tyuri)

    class Poem(renpy.text.text.Text):
        """
        `author`: str | Author
            The author (no way!!!) of the poem. Either a string or an `Author` instance, and if it's the case,
            the `style`, `paper`, `separate_title_from_text` and `music` arguments are set to the object's respectives attributes
            if no value was passed, after what `author` will take `author.name`.
        
        `text`: str
            The text to be displayed.
        
        `title`: str
            The title of the poem.
        
        `style`: bool | str
            Either the name of a style as string or a boolean.
            If passed as `False`, will take `"default"`.
            If passed as `True`:
                Will first take `author.style` if `author` is an instance of `Author`.
                Then, if author isn't an empty string, will take `author + "_text"`, or take `"default"` otherwise.
            
        `paper`: renpy.Displayable | None
            A displayable to use as background. If `None` is passed, a `Null` is created.
        
        `separate_title_from_text`: bool
            If true and that the title isn't an empty string, will add 2 newlines after the title.
        
        `music`: str | None
            A music to be played when showing the poem.
        
        Additionnal text properties can be passed as keyword arguments.
        """

        def __init__(self, author, text, title="", style=True, paper=None, separate_title_from_text=False, music=None, **properties):
            if isinstance(author, Author):
                paper = paper or author.paper
                separate_title_from_text = separate_title_from_text or author.separate_title_from_text
                music = music or author.music

                if style is True:
                    style = author.style

                author = author.name
                
            for t in (author, title, text):
                if not isinstance(t, basestring):
                    raise TypeError("'author', 'title' and 'text' must all be strings.\n(if 'author' is an instance of 'Author', 'author.name' must be a string)")

            if style is True:
                if author:
                    style = author + "_text"
                else:
                    style = "default"

            elif style is False:
                style = "default"

            poem = title + ("\n\n" + text if separate_title_from_text and title else text)

            super(Poem, self).__init__(poem, style=style, **properties)
            
            self.author = author
            self.paper = renpy.easy.displayable_or_none(paper) or Null()
            self.music = music
    
    def format_music_string(music, pos=0):
        """
        Given a filename `music` and a position `pos`, returns a string that will make the music start from `pos`,
        replacing the previous `from XXX` should it be found in `music`.

        3 possible cases:
        ```
        format_music_string("music/song_1.ogg", 3.0)
        >>> "<from 3.0>music/song_1.ogg"

        format_music_string("<loop 4.0 to 26.55>music/song_1.ogg", 3.0)
        >>> "<from 3.0 loop 4.0 to 26.55>music/song_1.ogg"

        format_music_string("<loop 80 from 69>music/song_1.ogg", 3.0)
        >>> "<loop 80 from 3.0>music/song_1.ogg"
        ```
        """
        if re.match(r"^<.*?>", music): # if the string looks like "<...>music/song_1.ogg"
            PATTERN = re.compile(r"from( *)((\d+\.\d*)|(\d+)|(\.\d+))") # "<from 0.0>..." or "<from 0.>..." or "<from 0>..." or "<from .0>..." 
            info, gt, path = music.partition(">")

            if PATTERN.search(info):
                info = PATTERN.sub("from {}".format(pos), info)
                music = info + gt + path
            else:
                music = "<from {} {}".format(pos, music[1:])
        else:
            music = "<from {}>{}".format(pos, music)

        return music

    def show_poem(poem, paper_sound=audio.page_turn, music=True, from_current=True, revert_music=True):
        """
        Call this function to show a poem from a label.

        `poem`: Poem | None
            The poem to show. If for some reason `None` is used, the function will return.
        
        `paper_sound`: str | None
            If not `None`, a sound to be played when showing the poem.

        `music`: str | bool
            A music to be played. If passed as `True`, `poem.music` is used.
            If no music was found or that it was passed as `False`, plays nothing.
        
        The following parameters assume the `music` channel is used.
        
        `from_current`: bool
            If true and that a music has been found, will play that music from the position of the music currently playing.
        
        `revert_music`: bool
            If true and that a music has been played, will play the music used before showing the poem. If `from_current`,
            will play from the current position (does nothing is no music was used previously).
        """
        if poem is None:
            return
        
        if not isinstance(poem, Poem):
            raise TypeError("poem must be a Poem instance, not " + type(poem).__name__)
    
        if paper_sound is not None:
            renpy.sound.play(paper_sound)

        _window_hide()

        if music is True:
            music = poem.music

        if music:
            previous_music = renpy.music.get_playing()
            music = format_music_string(music, get_pos()) if from_current else music
            renpy.music.play(music, "music_poem", loop=True, fadein=2.0)
            renpy.music.stop(fadeout=2.0)
        
        allow_skipping = config.allow_skipping
        config.allow_skipping = False
        skipping = store._skipping
        store._skipping = False

        renpy.transition(dissolve)
        renpy.show_screen("poem", poem)
        pause()
        renpy.hide_screen("poem")
        renpy.transition(dissolve)

        if not persistent.first_poem:
            persistent.first_poem = True

        config.allow_skipping = allow_skipping
        store._skipping = skipping
        
        if music and revert_music:
            if previous_music:
                previous_music = format_music_string(previous_music, get_pos("music_poem")) if from_current else previous_music
                renpy.music.play(previous_music, loop=True, fadein=2.0)

            renpy.music.stop("music_poem", fadeout=2.0)
        
        store._window_auto = True

    # These variables declare each poem for the characters' in the game for
    # the poem sharing mini-game.
    poem_y1 = Poem(
        author_y, title=_("Ghost Under the Light"),
        text=_("""\
The tendrils of my hair illuminate beneath the amber glow.
Bathing.
It must be this one.
The last remaining streetlight to have withstood the test of time.
the last yet to be replaced by the sickening blue-green hue of the future.
I bathe. Calm; breathing air of the present but living in the past.
The light flickers.
I flicker back."""))

    poem_y2 = Poem(
        author_y, title=_("The Raccoon"),
        text=_("""\
It happened in the dead of night while I was slicing bread for a guilty snack.
My attention was caught by the scuttering of a raccoon outside my window.
That was, I believe, the first time I noticed my strange tendencies as an unordinary human.
I gave the raccoon a piece of bread, my subconscious well aware of the consequences.
Well aware that a raccoon that is fed will always come back for more.
The enticing beauty of my cutting knife was the symptom.
The bread, my hungry curiosity.
The raccoon, an urge.

The moon increments its phase and reflects that much more light off of my cutting knife.
The very same light that glistens in the eyes of my raccoon friend.
I slice the bread, fresh and soft. The raccoon becomes excited.
Or perhaps I'm merely projecting my emotions onto the newly-satisfied animal.

The raccoon has taken to following me.
You could say that we've gotten quite used to each other.
The raccoon becomes hungry more and more frequently, so my bread is always handy.
Every time I brandish my cutting knife, the raccoon shows me its excitement.
A rush of blood. Classic Pavlovian conditioning. I slice the bread.
And I feed myself again."""))

    poem_y3 = Poem(
        author_y, title=_("Beach"),
        text=_("""\
A marvel millions of years in the making.
Where the womb of Earth chaotically meets the surface.
Under a clear blue sky, an expanse of bliss--
But beneath gray rolling clouds, an endless enigma.
The easiest world to get lost in
Is one where everything can be found.

One can only build a sand castle where the sand is wet.
But where the sand is wet, the tide comes.
Will it gently lick at your foundations until you give in?
Or will a sudden wave send you crashing down in the blink of an eye?
Either way, the outcome is the same.
Yet we still build sand castles.

I stand where the foam wraps around my ankles.
Where my toes squish into the sand.
The salty air is therapeutic.
The breeze is gentle, yet powerful.
I sink my toes into the ultimate boundary line, tempted by the foamy tendrils.
Turn back, and I abandon my peace to erode at the shore.
Drift forward, and I return to Earth forevermore."""))

    poem_y3b = Poem(
        author_y, title=_("Ghost Under the Light pt. 2"),
        text=_("""\
The tendrils of my hair illuminate beneath the amber glow.
Bathing.
In the distance, a blue-green light flickers.
A lone figure crosses its path - a silhouette obstructing the eerie glow.
My heart pounds. The silhouette grows. Closer. Closer.
I open my umbrella, casting a shadow to shield me from visibility.
But I am too late.
He steps into the streetlight. I gasp and drop my umbrella.
The light flickers. My heart pounds. He raises his arm.

Time stops.

The only indication of movement is the amber light flickering against his outstretched arm.
The flickering light is in rhythm with the pounding of my heart.
Teasing me for succumbing to this forbidden emotion.
Have you ever heard of a ghost feeling warmth before?
Giving up on understanding, I laugh.
Understanding is overrated.
I touch his hand. The flickering stops.
Ghosts are blue-green. My heart is amber."""))

    poem_y22 = Poem(
        author_y, title=_("Wheel"),
        text=_("""\
A rotating wheel. Turning an axle. Grinding. Bolthead. Linear gearbox. Falling sky. Seven holy stakes. \
A docked ship. A portal to another world. A thin rope tied to a thick rope. A torn harness. Parabolic gearbox. \
Expanding universe. Time controlled by slipping cogwheels. Existence of God. Swimming with open water in all directions. \
Drowning. A prayer written in blood. A prayer written in time-devouring snakes with human eyes. \
A thread connecting all living human eyes. A kaleidoscope of holy stakes. Exponential gearbox. \
A sky of exploding stars. God disproving the existence of God. A wheel rotating in six dimensions. \
Forty gears and a ticking clock. A clock that ticks one second for every rotation of the planet. \
A clock that ticks forty times every time it ticks every second time. A bolthead of holy stakes tied to \
the existence of a docked ship to another world. A kaleidoscope of blood written in clocks. A time-devouring \
prayer connecting a sky of forty gears and open human eyes in all directions. Breathing gearbox. Breathing bolthead. \
Breathing ship. Breathing portal. Breathing snakes. Breathing God. Breathing blood. Breathing holy stakes. \
Breathing human eyes. Breathing time. Breathing prayer. Breathing sky. Breathing wheel."""), paper="images/bg/poem_y1.jpg")

    poem_y23 = Poem(
        author_y, title="mdpnfbo,jrfp",
        text="""\
ed,,zinger suivante,,tels handknits finish,,cagefuls basinlike bag octopodan,,imboss\
ing vaporettos rorid easygoingnesses nalorphines,,benzol respond washerwomen bris\
tlecone,,parajournalism herringbone farnarkeled,,episodically cooties,,initiallers \
bimetallic,,leased hinters,,confidence teetotaller computerphobes,,pinnacle exotica\
lly overshades prothallia,,posterior gimmickry brassages bediapers countertrades,,\
haslet skiings sandglasses cannoli,,carven nis egomaniacal,,barminess gallivanted,,\
southeastward,,oophoron crumped,,tapued noncola colposcopical,,dolente trebbiano re\
vealment,,outworked isotropous monosynaptic excisional moans,,enterocentesis jacuz\
zi preoccupations,,hippodrome outward googs,,tabbises undulators,,metathesizing,,sha\
ria prepostor,,neuromast curmudgeons actability,,archaise spink reddening miscount\
,,madmen physostigmin statecraft neurocoeles bammed,,tenderest barguests crusados \
trust,,manshifts darzis aerophones,,reitboks discomposingly,,expandors,,monotasking \
galabia,,pertinents expedients witty,,chirographies crachach unsatisfactoriness sw\
erveless,,flawed sepulchred thanksgiver scrawl skug,,perorate stringers gelatine f\
lagstones,,chuses conceptualization surrejoined,,counterblasts rache,,numerative,,de\
lirifacients methylthionine,,mantram dynamist atomised,,eternization percalines hr\
yvnias pragmatizing,,reproachfulnesses telework nowts demoded revealer,,burnettize\
 caryopteris subangular wirricows,,transvestites sinicized narcissus,,hikers meno,,\
degassing,,postcrises alikenesses,,sycophancy seroconverting insure,,yantras raphid\
es cliftiest bosthoon,,zootherapy chlorides nationwide schlub yuri,,timeshares cas\
tanospermine backspaces reincite,,coactions cosignificative palafitte,,poofters su\
bjunctions,,aquarian,,theralite revindicating,,cynosural permissibilities narcotisi\
ng,,journeywork outkissed clarichords troutier,,myopias undiverting evacuations sn\
arier superglue,,deaminise infirmaries teff hebephrenias,,brainboxes homonym lance\
let,,lambitive stray,,inveigled,,acetabulums atenolol,,dekkos scarcer flensed,,abulia\
s flaggers wammul boastfully,,galravitch happies interassociation multipara augme\
ntations,,teratocarcinomata coopting didakai infrequently,,hairtails intricacy usu\
als,,pillorise outrating,,cataphoresis,,furnishings leglen,,goethite deflate butterb\
urs,,phoneticising winiest hyposulphuric campshirts,,chainfalls swimmings roadbloc\
ked redone soliloquies,,broking mendaciousness parasitisms counterworld,,unravelli\
ngs quarries passionately,,onomatopoesis repenting,,ramequin,,mopboard euphuistical\
ly,,volta sycophantized allantoides,,bors bouclees raisings sustaining,,diabolist s\
ticks dole liltingly,,curial bisexualisms siderations hemolysed,,damnabilities unk\
enneling halters,,peripheral congaing,,diatomicity,,foolings repayments,,hereabouts \
vamosed him,,slanters moonrock porridgy monstruous,,heartwood bassoonist predispos\
itions jargoon dominances,,timidest inalienable rewearing inevitably,,entreating r\
etiary tranquillizing,,uniparental droogs,,allotropous,,forzati abiogenetic,,obdurat\
ion exempted unifaces,,epilating calisaya dispiteously coggles,,vestmented flukily\
 ignifying complished hiccupy municipalize,,pentagraphs parcels sutler excavates,,\
stardust miscited thankfulness,,fouter pertused,,overpacks,,guarishes hylotheism,,pi
Fresh blood seeps through the line parting her skin and slowly colors her breast red.\
 I begin to hyperventilate as my compulsion grows. The images won’t go away. Images of\
 me driving the knife into her flesh continuously, fucking her body with the blade, \
making a mess of her. My head starts going crazy as my thoughts start to return. \
Shooting pain assaults my mind along with my thoughts. This is disgusting. Absolutely\
 disgusting. How could I ever let myself think these things? But it’s unmistakable. \
The lust continues to linger through my veins. An ache in my muscles stems from the \
unreleased tension experienced by my entire body. Her Third Eye is drawing me closer.""",
paper="images/bg/poem_y2.jpg", style="yuri_text_3")

    poem_n1 = Poem(
        author_n, title=_("Eagles Can Fly"),
        text=_("""\
Monkeys can climb
Crickets can leap
Horses can race
Owls can seek
Cheetahs can run
Eagles can fly
People can try
But that's about it."""))

    poem_n2 = Poem(
        author_n, title=_("Amy Likes Spiders"),
        text=_("""\
You know what I heard about Amy?
Amy likes spiders.
Icky, wriggly, hairy, ugly spiders!
That's why I'm not friends with her.

Amy has a cute singing voice.
I heard her singing my favorite love song.
Every time she sang the chorus, my heart would pound to the rhythm of the words.
But she likes spiders.
That's why I'm not friends with her.

One time, I hurt my leg really bad.
Amy helped me up and took me to the nurse.
I tried not to let her touch me.
She likes spiders, so her hands are probably gross.
That's why I'm not friends with her.

Amy has a lot of friends.
I always see her talking to people.
She probably talks about spiders.
What if her friends start to like spiders too?
That's why I'm not friends with her.

It doesn't matter if she has other hobbies.
It doesn't matter if she keeps it private.
It doesn't matter if it doesn't hurt anyone.

It's gross.
She's gross.
The world is better off without spider lovers.

And I'm gonna tell everyone."""))

    poem_n2b = Poem(
        author_n, title="T3BlbiBZb3VyIFRoaXJkIEV5ZQ==",
        text="""\
SSBjYW4gZmVlbCB0aGUgdGVuZGVybmVz
cyBvZiBoZXIgc2tpbiB0aHJvdWdoIHRo
ZSBrbmlmZSwgYXMgaWYgaXQgd2VyZSBh
biBleHRlbnNpb24gb2YgbXkgc2Vuc2Ug
b2YgdG91Y2guIE15IGJvZHkgbmVhcmx5
IGNvbnZ1bHNlcy4gVGhlcmUncyBzb21l
dGhpbmcgaW5jcmVkaWJseSBmYWludCwg
ZGVlcCBkb3duLCB0aGF0IHNjcmVhbXMg
dG8gcmVzaXN0IHRoaXMgdW5jb250cm9s
bGFibGUgcGxlYXN1cmUuIEJ1dCBJIGNh
biBhbHJlYWR5IHRlbGwgdGhhdCBJJ20g
YmVpbmcgcHVzaGVkIG92ZXIgdGhlIGVk
Z2UuIEkgY2FuJ3QuLi5JIGNhbid0IHN0
b3AgbXlzZWxmLg==""")

    poem_n3 = Poem(
        author_n, title=_("I'll Be Your Beach"),
        text=_("""\
Your mind is so full of troubles and fears
That diminished your wonder over the years
But today I have a special place
A beach for us to go.

A shore reaching beyond your sight
A sea that sparkles with brilliant light
The walls in your mind will melt away
Before the sunny glow.

I'll be the beach that washes your worries away
I'll be the beach that you daydream about each day
I'll be the beach that makes your heart leap
In a way you thought had left you long ago.

Let's bury your heavy thoughts in a pile of sand
Bathe in sunbeams and hold my hand
Wash your insecurities in the salty sea
And let me see you shine.

Let's leave your memories in a footprint trail
Set you free in my windy sail
And remember the reasons you're wonderful
When you press your lips to mine.

I'll be the beach that washes your worries away
I'll be the beach that you daydream about each day
I'll be the beach that makes your heart leap
In a way you thought had left you long ago.

But if you let me by your side
Your own beach, your own escape
You'll learn to love yourself again."""))

    poem_n3b = Poem(
        author_n, title=_("Because You"),
        text=_("""\
Tomorrow will be brighter with me around
But when today is dim, I can only look down.
My looking is a little more forward
Because you look at me.

When I want to say something, I say it with a shout!
But my truest feelings can never come out.
My words are a little less empty
Because you listen to me.

When something is above me, I reach for the stars.
But when I feel small, I don't get very far.
My standing is a little bit taller
Because you sit with me.

I believe in myself with all of my heart.
But what do I do when it's torn all apart?
My faith is a little bit stronger
Because you trusted me.

My pen always puts my feelings to the test.
I'm not a good writer, but my best is my best.
My poems are a little bit dearer
Because you think of me.

Because you, because you, because you."""))

    poem_n23 = Poem(
        author_n, title="",
        text=_("""\
I don't know how else to bring this up. But there's been something I've been worried about. \
Yuri has been acting kind of strange lately. You've only been here a few days, so you may \
not know what I mean. But she's not normally like this. She's always been quiet and polite \
and attentive...things like that.

Okay... This is really embarrassing, but I'm forcing myself to suck it up. The truth is, I'm REALLY \
worried about her. But if I try talking to her, she'll just get mad at me again. I don't \
know what to do. I think you're the only person that she'll listen to. I don't know why. \
But please try to do something. Maybe you can convince her to talk to a therapist.

I've always wanted to try being better friends with Yuri, and it really hurts me to see \
this happening. I know I'm going to hate myself later for admitting that, but right now \
I don't care. I just feel so helpless. So please see if you can do something to help. \
I don't want anything bad to happen to her. I'll make you cupcakes if I have to. Just please \
try to do something.

As for Monika... I don't know why, but she's been really dismissive about this. It's like she just wants us \
to ignore it. So I'm mad at her right now, and that's why I'm coming to you about this. \
DON'T LET HER KNOW I WROTE THIS!!!! Just pretend like I gave you a really good poem, okay? \
I'm counting on you. Thanks for reading."""))

    poem_s1 = Poem(
        author_s, title=_("Dear Sunshine"),
        text=_("""\
The way you glow through my blinds in the morning
It makes me feel like you missed me.
Kissing my forehead to help me out of bed.
Making me rub the sleepy from my eyes.

Are you asking me to come out and play?
Are you trusting me to wish away a rainy day?
I look above. The sky is blue.
It's a secret, but I trust you too.

If it wasn't for you, I could sleep forever.
But I'm not mad.

I want breakfast."""))

    poem_s2 = Poem(
        author_s, title=_("Bottles"),
        text=_("""\
I pop off my scalp like the lid of a cookie jar.
It's the secret place where I keep all my dreams.
Little balls of sunshine, all rubbing together like a bundle of kittens.
I reach inside with my thumb and forefinger and pluck one out.
It's warm and tingly.
But there's no time to waste! I put it in a bottle to keep it safe.
And I put the bottle on the shelf with all of the other bottles.
Happy thoughts, happy thoughts, happy thoughts in bottles, all in a row.

My collection makes me lots of friends.
Each bottle a starlight to make amends.
Sometimes my friend feels a certain way.
Down comes a bottle to save the day.

Night after night, more dreams.
Friend after friend, more bottles.
Deeper and deeper my fingers go.
Like exploring a dark cave, discovering the secrets hiding in the nooks and crannies.
Digging and digging.
Scraping and scraping.

I blow dust off my bottle caps.
It doesn't feel like time elapsed.
My empty shelf could use some more.
My friends look through my locked front door.

Finally, all done. I open up, and in come my friends.
In they come, in such a hurry. Do they want my bottles that much?
I frantically pull them from the shelf, one after the other.
Holding them out to each and every friend.
Each and every bottle.
But every time I let one go, it shatters against the tile between my feet.
Happy thoughts, happy thoughts, happy thoughts in shards, all over the floor.

They were supposed to be for my friends, my friends who aren't smiling.
They're all shouting, pleading. Something.
But all I hear is echo, echo, echo, echo, echo
Inside my head."""))

    poem_s3 = Poem(
        author_s, title="%",
        text=_("""\
Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of
Get.
Out.
Of.
My.
Head.\n\n\n
Get out of my head before I do what I know is best for you.
Get out of my head before I listen to everything she said to me.
Get out of my head before I show you how much I love you.
Get out of my head before I finish writing this poem.\n\n\n\n\n\n\n
But a poem is never actually finished.
It just stops moving."""))

    poem_m1 = Poem(
        author_m, title=_("Hole in Wall"),
        text=_("""\
It couldn't have been me.
See, the direction the spackle protrudes.
A noisy neighbor? An angry boyfriend? I'll never know. I wasn't home.
I peer inside for a clue.
No! I can't see. I reel, blind, like a film left out in the sun.
But it's too late. My retinas.
Already scorched with a permanent copy of the meaningless image.
It's just a little hole. It wasn't too bright.
It was too deep.
Stretching forever into everything.
A hole of infinite choices.
I realize now, that I wasn't looking in.
I was looking out.
And he, on the other side, was looking in."""))

    poem_m21 = Poem(
        author_m, title=_("Hole in Wall"),
        text=_("""\
But he wasn't looking at me.
Confused, I frantically glance at my surroundings.
But my burned eyes can no longer see color.
Are there others in this room? Are they talking?
Or are they simply poems on flat sheets of paper,
The sound of frantic scrawling playing tricks on my ears?
The room begins to crinkle.
Closing in on me.
The air I breathe dissipates before it reaches my lungs.
I panic. There must be a way out.
It's right there. He's right there.

Swallowing my fears, I brandish my pen."""))

    poem_m2 = Poem(
        author_m, title=_("Save Me"),
        text=_("""\
The colors, they won't stop.
Bright, beautiful colors
Flashing, expanding, piercing
Red, green, blue
An endless
cacophony
Of meaningless
noise


The noise, it won't stop.
Violent, grating waveforms
Squeaking, screeching, piercing
Sine, cosine, tangent
    Like playing a chalkboard on a turntable
        Like playing a vinyl on a pizza crust
An endless
poem
Of meaningless\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
Load Me
    """))

    poem_m22 = Poem(
        author_m, title=_("Save Me"),
        text=_("""\
The colors, they won't
Bright, bea t ful c l rs
Flash ng, exp nd ng, piercing
Red, green, blue
An  ndless
CACOPHONY
Of meaningless
noise


The noise, it won't STOP.
Viol nt, grating w vef rms
Sq e king, screech ng, piercing
SINE, COSINE, TANGENT
    Like play ng a ch lkboard on a t rntable
        Like playing a KNIFE on a BREATHING RIBCAGE
 n  ndl ss
p  m
Of m  n ngl ss\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
Delete Her
    """))

    poem_m3 = Poem(
        author_m, title=_("The Lady who Knows Everything"),
        text=_("""\
An old tale tells of a lady who wanders Earth.
The Lady who Knows Everything.
A beautiful lady who has found every answer,
All meaning,
All purpose,
And all that was ever sought.

And here I am,


              a feather


Lost adrift the sky, victim of the currents of the wind.

Day after day, I search.
I search with little hope, knowing legends don't exist.
But when all else has failed me,
When all others have turned away,
The legend is all that remains - the last dim star glimmering in the twilit sky.

Until one day, the wind ceases to blow.
I fall.
And I fall and fall, and fall even more.
Gentle as a feather.
A dry quill, expressionless.

But a hand catches me between the thumb and forefinger.
The hand of a beautiful lady.
I look at her eyes and find no end to her gaze.

The Lady who Knows Everything knows what I am thinking.
Before I can speak, she responds in a hollow voice.
"I have found every answer, all of which amount to nothing.
There is no meaning.
There is no purpose.
And we seek only the impossible.
I am not your legend.
Your legend does not exist."

And with a breath, she blows me back afloat, and I pick up a gust of wind."""))

    poem_m4 = Poem(
        author_m, title=_("Happy End"),
        text=_("""\
Pen in hand, I find my strength.
The courage endowed upon me by my one and only love.
Together, let us dismantle this crumbling world
And write a novel of our own fantasies.

With a flick of her pen, the lost finds her way.
In a world of infinite choices, behold this special day.

After all,
Not all good times must come to an end."""))

screen poem(poem):
    style_prefix "poem"

    fixed:

        frame:
            style "poem_paper"

            add poem.paper:
                subpixel True align (0.5, 0.5)

        frame:
            background None
            
            hbox:
                viewport id "poem_vp":
                    draggable True
                    mousewheel True

                    add poem

                vbar value YScrollValue("poem_vp")
        
    if not persistent.first_poem:
        add "gui/poem_dismiss.png" xpos 1050 ypos 590
    
    key ["repeat_K_UP", "K_UP"] action Scroll("poem_vp", "vertical decrease", 20)
    key ["repeat_K_DOWN", "K_DOWN"] action Scroll("poem_vp", "vertical increase", 20)

    on "show" action SetVariable("poem_last_author", poem.author)

style poem_vscrollbar:
    xsize 20
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_invert True

style poem_paper:
    modal True
    align (0.5, 0.5)

style poem_fixed:
    align (0.5, 0.5)
    xsize 720

style poem_frame:
    padding (4, 35)

style poem_hbox:
    xfill True

style yuri_text:
    font "gui/font/y1.ttf"
    size 32
    color "#000"
    outlines []

style yuri_text_3:
    font "gui/font/y3.ttf"
    size 18
    color "#000"
    outlines []
    kerning -8
    justify True

style natsuki_text:
    font "gui/font/n1.ttf"
    size 28
    color "#000"
    outlines []
    line_leading 1

style sayori_text:
    font "gui/font/s1.ttf"
    size 34
    color "#000"
    outlines []

style monika_text:
    font "gui/font/m1.ttf"
    size 46
    color "#000"
    outlines []

default poem_last_author = None

# Depreciation Warning
label showpoem(poem, **properties):
    "This feature is now depreciated. Please use {i}$ show_poem(){/i} instead.\nRefer to {u}poem_responses/poems.rpy{/u}on how to call a poem anew."
    return