# pragmatic segmenter

pragmatic segmenter was implemented in Ruby. It did some preprocessing, which is nice. But it is written in Ruby, a language I do not know, which is either a con or a reason to learn a new programming language.

-----																	
Flaws
-----
*Umbro Cup er en oppvarmingsturnering til håndball-EM i Sveits, hvor Norge skal spille åpningskamp mot Russland den 26.
januar.* (This gets marked as separate sentences, but it seems they were says 26 of January with a period)

*I 2001 avgjorde administrasjonen i det Kvite Hus at sanksjonane mot India skulle opphevast, som ein del av arbeidet med å skaffe nye partnarar og støttespelarar etter terrorangrepa i New York 11.
september same året.* (Another date messed up)

*Kva er grunnlaget for staten sin legitimitet, og kva er grunnen til at staten kollapsar?
spurte professoren.* (From google translate, it seems that this should be one sentence)

--------------------------------------------------
Things that were pleasantly identified correctly
--------------------------------------------------
*Met.no*

*miside.no*

*www.miside.no.* (noted this as the end of a sentence)

*...uttalte leiaren av FSF, Richard M. Stallman, at den mest...* (This gets correctly ignored as not a sentence break.)

*...pp måndag (16.01) eit utkast til d...* (this too)

*...handlar mot selskapet som reklamerar med «Ingen legebesøk!»*

*helsekøa på Lærdal Sjukehus, melder Dagbladet.no og Firda.no.*

*har vorte samde om å møtast til forhandlingar i Sveits. Det meldte NRK P2 tidlegare i dag (25.01).*

*Klokken 13:55 opplyste politiet om at fem personer var skadet som følge av brannen.
Fire av disse er kjørt til legevakta og en til Ullevål Sykehus
200 personer i området ble evakuert på grunn av giftig røyk fra brennede isopor.*
(I'm very impressed that the middle sentence (without punctuation) gets separated from the one following it. From Google translate, it seems that they should be separated. )

*3. februar 2006* (The day-dot-month situation happened sentence-initially so this time it was not fooled)

*Når presidenten i Sambandsstatane (USA), George W. Bush no førebur seg på ei vitjing til India den 2.
mars, arbeidar diplomatar frå begge land hardt for å verte samde om ein USA-Indisk atomkraft-avtale på førehand.*
(The second sentence starts with a lower-case letter, yet it identifies sep sentences)


# Punkt

It calls things pickles. Why not.
Did not do so much preprocessing. There's still quite a bit of junk tags and linebreaks in the text.

Note: I used the swedish pickle, but this might be Norwegian? The text speaks of Norwegian issues a lot.
-----																	
Flaws
-----
The lack of preprocessing is debatably a flaw.

*Mellom anna krev han at «hvis det er den minste åpning for dette i norsk lov, så må loven endres, og det fort!»\nI pressemeldinga frå ungdomsorganisasjonen til Senterpartiet vert det trekt fram at nettapoteket ei stund har marknadsført seg gjennom Deiligst.no, ein nettstad som er særs populær blant norsk ungdom.* (This looks like it should be two sentences, but that is lost in the linebreak character I think. )

*Merk: Omsetjinga i den her versjonen er særs ufullstendig\n\nUSA og India nærmar seg atomkraft-avtale:\n<onlyinclude>/Når presidenten i Sambandsstatane (USA), George W. Bush no førebur seg på ei vitjing til India den 2. mars, arbeidar diplomatar frå begge land hardt for å verte samde om ein USA-Indisk atomkraft-avtale på førehand.<onlyinclude>\nDen kraftige veksten i indisk økonomi, med heile 8\xa0% årleg vekst, har ført til store utgifter for både den sivile og militære infrastrukturen i landet, men få av dei indiske kontraktene har hamna hos verksemder med hovudsete i USA.* (this was all marked as one sentence, probably (again) because of the lack of preprocessing. I'm calling this a flaw, you could argue that I'm the one with the flaw because I didn't preprocess it myself.)

--------------------------------------------------
Things were pleasantly identified correctly
--------------------------------------------------
*Ferje sank i Rødehavet:\n<onlyinclude>Den egyptiske ferja al-Salam Boccaccio 98 sank i Rødehavet 2. februar 2006 på vei fra Duba i Saudi-Arabia til byen Safaga sør i Egypt* (it looks like Punkt is handling dates better)

*Umbro Cup er en oppvarmingsturnering til håndball-EM i Sveits, hvor Norge skal spille åpningskamp mot Russland den 26. januar.* (again, date is correct)

the same as the Ruby one, unless mentioned in the flaws section
