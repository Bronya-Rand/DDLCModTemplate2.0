# Copyright 2019-2025 Azariel Del Carmen (bronya_rand). All rights reserved.
# This file contains the Python code for displaying poems in DDLC.

# The logic for displaying poems has been changed drastically compared to the original
# game to allow for more poem management.
# It also follows the Ren'Py approach of using the new `_ren.py` file for Python code.

# For the poem display code, see `poems.rpy` in the `poem_responses` directory.

## This import is not used when the game is running, but exists so IDEs reports
## one warning than multiple.
import re
import typing
from game.definitions.py.core_ren import pause, persistent, store
import renpy  # type: ignore

"""renpy
init python:
"""


class PoemAuthor(object):
    """
    A class used to represent a DDLC character's poem author.
    """

    def __init__(
        self,
        name: str,
        style: bool | str = True,
        paper: str = "images/bg/poem.jpg",
        separate_title_from_text: bool = True,
        music: str | None = None,
    ):
        """
        Initializes the poem author with the given parameters.

        :param name: The name of the poem author.
        :param style: Whether to apply a specific style to the poem.
        :param paper: The background image for the poem.
        :param separate_title_from_text: Whether to separate the title from the text.
        :param music: The music to play during the poem.

        :type name: str
        :type style: bool
        :type paper: str
        :type separate_title_from_text: bool
        :type music: str | None
        """
        self.name = name
        self.style = style
        self.paper = paper
        self.separate_title_from_text = separate_title_from_text
        self.music = music


class Poem(renpy.text.text.Text):
    """
    A class used to represent a DDLC character's poem.
    """

    def __init__(
        self,
        author: PoemAuthor | str,
        text: str = "",
        title: str = "",
        style: bool | str = True,
        paper: str = "images/bg/poem.jpg",
        separate_title_from_text: bool = True,
        music: str | None = None,
        **properties,
    ):
        """
        Initializes the poem with the given parameters.

        :param author: The author of the poem.
        :param text: The text of the poem.
        :param title: The title of the poem.
        :param style: Whether to apply a specific style to the poem.
        :param paper: The background image for the poem.
        :param separate_title_from_text: Whether to separate the title from the text.
        :param music: The music to play during the poem.

        :type author: PoemAuthor | str
        :type text: str | None
        :type title: str
        :type style: bool
        :type paper: str
        :type separate_title_from_text: bool
        :type music: str | None
        """
        if isinstance(author, PoemAuthor):
            paper = paper or author.paper
            separate_title_from_text = (
                separate_title_from_text or author.separate_title_from_text
            )
            music = music or author.music

            if style is True:
                style = author.style

            author = author.name

        for arg in (author, text, title):
            if not isinstance(arg, str):
                raise TypeError(f"{arg} must be type str, not {type(arg).__name__}")

        if style is True:
            if author:
                style = "%s_text" % author
            else:
                style = "default"
        else:
            style = "default"

        poem = (
            "%s\n\n%s" % (title, text) if separate_title_from_text and title else text
        )

        super().__init__(poem, style=style, **properties)

        self.author = author
        self.paper = renpy.easy.displayable_or_none(paper) or renpy.Null()
        self.music = music

    def format_music_str(self, music: str, pos: int = 0):
        """
        Returns a formatted music string during and after the poem.

        :param music: The music track to format.
        :param pos: The position in the music track to start playing.

        :type music: str
        :type pos: int

        :return music: A formatted music string.
        :rtype: str
        """

        stripped_song = music.rpartition(">")[2]

        loop_pattern = re.compile(r"loop\s+\d+\.\d+")
        to_pattern = re.compile(r"to\s+\d+\.\d+")

        loop_match = loop_pattern.search(music)
        loop_value = loop_match.group(0) if loop_match else ""

        to_match = to_pattern.search(music)
        to_value = to_match.group(0) if to_match else ""

        return f"<from {pos} {loop_value} {to_value}>{stripped_song}"

        

    def show(
        self,
        img: str | None = None,
        at_list: list = [store.i11],
        paper_sound: str | None = store.audio.page_turn,
        music: str | bool = True,
        from_current: bool = True,
        revert_music: bool = True,
        testing: bool = False,
    ):
        """
        Displays the poem to the Poem Response screen.

        :param paper_sound: The sound to play when the poem is displayed.
        :param music: Whether to play the music associated with the poem.
        :param from_current: Whether to start the music from the current position of the previous music track.
        :param revert_music: Whether to revert the music to the previous track after the poem is displayed.
        :param testing: Unused in DDLC. Used for GitHub Actions testing purposes.

        :type paper_sound: str | None
        :type music: str | bool
        :type from_current: bool
        :type revert_music: bool
        :type testing: bool
        """
        if not testing:
            previous_music = None

            if paper_sound is not None:
                renpy.sound.play(paper_sound, channel="page_turn", loop=False)

            _window_hide()  # type: ignore # noqa: F821

            if music is True:
                poem_track = self.music or None
            else:
                poem_track = music or None

            if poem_track:
                previous_music = renpy.music.get_playing()
                music = (
                    self.format_music_str(poem_track, renpy.music.get_pos())
                    if from_current
                    else poem_track
                )
                renpy.music.play(music, channel="poem", loop=True, fadeout=0.5)
                renpy.music.stop(fadeout=2.0)

            allow_skipping = renpy.config.allow_skipping
            renpy.config.allow_skipping = False
            skipping = store._skipping
            store._skipping = False

            renpy.transition(store.dissolve)
            renpy.show_screen("poem", self)
            pause()

            if img:
                if isinstance(self.author, PoemAuthor):
                    renpy.hide(self.author.name)
                else:
                    renpy.hide(self.author)
                renpy.show(img, at_list=at_list)

            renpy.hide_screen("poem")
            renpy.transition(store.dissolve)

            renpy.config.allow_skipping = allow_skipping
            store._skipping = skipping

            if poem_track and revert_music:
                if previous_music:
                    previous_music = (
                        self.format_music_str(previous_music, renpy.music.get_pos(channel="poem"))
                        if from_current
                        else previous_music
                    )
                    renpy.music.play(previous_music, loop=True, fadein=2.0)

                renpy.music.stop("poem", fadeout=2.0)

            renpy._window_auto = True

        if not persistent.first_poem:
            persistent.first_poem = True


class PoemResponseDB(object):
    """
    A class used to represent a database of poems.
    """

    def __init__(self):
        """
        Initializes the poem response database.
        """
        self.poems: dict[str, Poem] = {}

    def add_poem(
        self,
        identifier: str,
        author: PoemAuthor,
        title: str,
        text: str,
        style: bool | str = True,
        paper: str = "images/bg/poem.jpg",
        separate_title_from_text: bool = True,
        music: str | None = None,
        translate: typing.Literal["all", "title", "text", "none"] = "all",
    ):
        """
        Adds a poem to the database.

        :param identifier: The unique identifier for the poem.
        :param author: The author of the poem.
        :param title: The title of the poem.
        :param text: The text of the poem.
        :param style: Whether to apply a specific style to the poem.
        :param paper: The background image for the poem.
        :param separate_title_from_text: Whether to separate the title from the text.
        :param music: The music to play during the poem.
        :param translate: Whether to let Ren'Py translate the poem text.

        :type identifier: str
        :type author: PoemAuthor
        :type title: str
        :type text: str
        :type style: bool | str
        :type paper: str
        :type separate_title_from_text: bool
        :type music: str | None
        :type translate: typing.Literal["all", "title", "text", "none"]
        """
        self.poems[identifier] = Poem(
            author=author,
            title=store._(title) if translate in ["all", "title"] else title,
            text=store._(text) if translate in ["all", "text"] else text,
            style=style,
            paper=paper,
            separate_title_from_text=separate_title_from_text,
            music=music,
        )

    def get_poem(self, identifier: str) -> Poem:
        """
        Retrieves a poem from the database by its identifier.

        :param identifier: The unique identifier for the poem.

        :type identifier: str

        :return poem: The poem if found
        :rtype: Poem
        :raise ValueError: If the poem with the given identifier does not exist.
        """
        if identifier in self.poems:
            return self.poems[identifier]
        raise ValueError(f"Poem with identifier '{identifier}' not found.")

    def get_poems(self) -> list[str]:
        """
        Returns a list of all poems in the database.

        :return: A list of all poems.
        :rtype: list[Poem]
        """
        return list(self.poems.keys())

    def show_poem(self, identifier: str, img: str | None = None, **kwargs):
        """
        Displays a poem from the database by its identifier.

        :param identifier: The unique identifier for the poem.
        :param kwargs: Additional keyword arguments to pass to the `show` method of the Poem class.

        :type identifier: str
        """
        poem = self.get_poem(identifier)
        if poem:
            poem.show(img=img, **kwargs)
        else:
            raise ValueError(f"Poem with identifier '{identifier}' not found.")


# Initialize the Poem database and authors.
poem_db = PoemResponseDB()

author_s = PoemAuthor("sayori", music=store.audio.tsayori)
author_n = PoemAuthor("natsuki", music=store.audio.tnatsuki)
author_y = PoemAuthor("yuri", music=store.audio.tyuri)
author_m = PoemAuthor("monika", music=store.audio.tmonika)

## Yuri's Poems
poem_db.add_poem(
    "poem_y1",
    author_y,
    title="Ghost Under the Light",
    text="""\
The tendrils of my hair illuminate beneath the amber glow.
Bathing.
It must be this one.
The last remaining streetlight to have withstood the test of time.
the last yet to be replaced by the sickening blue-green hue of the future.
I bathe. Calm; breathing air of the present but living in the past.
The light flickers.
I flicker back.""",
)

poem_db.add_poem(
    "poem_y2",
    author_y,
    title="The Raccoon",
    text="""\
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
And I feed myself again.""",
)

poem_db.add_poem(
    "poem_y3",
    author_y,
    title="Beach",
    text="""\
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
Drift forward, and I return to Earth forevermore.""",
)

poem_db.add_poem(
    "poem_y3b",
    author_y,
    title="Ghost Under the Light pt. 2",
    text="""\
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
Ghosts are blue-green. My heart is amber.""",
)

## Yuri's Act 2 Poems
poem_db.add_poem(
    "poem_y22",
    author_y,
    title="Wheel",
    text="""\
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
Breathing human eyes. Breathing time. Breathing prayer. Breathing sky. Breathing wheel.""",
    paper="images/bg/poem_y1.jpg",
)

poem_db.add_poem(
    "poem_y23",
    author_y,
    title="mdpnfbo,jrfp",
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
    paper="images/bg/poem_y2.jpg",
    style="yuri_text_3",
    translate="none",
)

## Natsuki's Poems
poem_db.add_poem(
    "poem_n1",
    author_n,
    title="Eagles Can Fly",
    text="""\
Monkeys can climb
Crickets can leap
Horses can race
Owls can seek
Cheetahs can run
Eagles can fly
People can try
But that's about it.""",
)

poem_db.add_poem(
    "poem_n2",
    author_n,
    title="Amy Likes Spiders",
    text="""\
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

And I'm gonna tell everyone.""",
)

poem_db.add_poem(
    "poem_n3",
    author_n,
    title="I'll Be Your Beach",
    text="""\
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
You'll learn to love yourself again.""",
)

poem_db.add_poem(
    "poem_n3b",
    author_n,
    title="Because You",
    text="""\
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

Because you, because you, because you.""",
)

## Natsuki's Act 2 Poems
poem_db.add_poem(
    "poem_n2b",
    author_n,
    title="T3BlbiBZb3VyIFRoaXJkIEV5ZQ==",
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
b3AgbXlzZWxmLg==""",
    translate="none",
)

poem_db.add_poem(
    "poem_n23",
    author_n,
    title="",
    text="""\
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
I'm counting on you. Thanks for reading.""",
    translate="text",
)

## Sayori's Poems
poem_db.add_poem(
    "poem_s1",
    author_s,
    title="Dear Sunshine",
    text="""\
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

I want breakfast.""",
)

poem_db.add_poem(
    "poem_s2",
    author_s,
    title="Bottles",
    text="""\
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
Inside my head.""",
)

poem_db.add_poem(
    "poem_s3",
    author_s,
    title="%",
    text="""\
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
It just stops moving.""",
    translate="text",
)

## Monika's Poems
poem_db.add_poem(
    "poem_m1",
    author_m,
    title="Hole in Wall",
    text="""\
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
And he, on the other side, was looking in.""",
)

poem_db.add_poem(
    "poem_m2",
    author_m,
    title="Save Me",
    text="""\
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
    """,
)

poem_db.add_poem(
    "poem_m3",
    author_m,
    title="The Lady who Knows Everything",
    text="""\
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

And with a breath, she blows me back afloat, and I pick up a gust of wind.""",
)

poem_db.add_poem(
    "poem_m4",
    author_m,
    title="Happy End",
    text="""\
Pen in hand, I find my strength.
The courage endowed upon me by my one and only love.
Together, let us dismantle this crumbling world
And write a novel of our own fantasies.

With a flick of her pen, the lost finds her way.
In a world of infinite choices, behold this special day.

After all,
Not all good times must come to an end.""",
)

## Monika's Act 2 Poems
poem_db.add_poem(
    "poem_m21",
    author_m,
    title="Hole in Wall",
    text="""\
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

Swallowing my fears, I brandish my pen.""",
)

poem_db.add_poem(
    "poem_m22",
    author_m,
    title="Save Me",
    text="""\
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
    """,
)
