from Huffman import Huffman
import pprint

if __name__ == "__main__":
    # sample = "Hellow world my name is baek.seungjae"
    sample = """First things first
I'ma say all the words inside my head
I'm fired up and tired of the way that things have been, oh ooh
The way that things have been, oh ooh
Second thing second
Don't you tell me what you think that I can be
I'm the one at the sail, I'm the master of my sea, oh ooh
The master of my sea, oh ooh
I was broken from a young age
Taking my sulking to the masses
Write down my poems for the few
That looked at me, took to me, shook to me, feeling me
Singing from heartache from the pain
Taking my message from the veins
Speaking my lesson from the brain
Seeing the beauty through the
You made me a, you made me a believer, believer
(Pain, pain)
You break me down, you build me up, believer, believer
(Pain)
Oh let the bullets fly, oh let them rain
My life, my love, my drive, it came from
(Pain)
You made me a, you made me a believer, believer
Third things third
Send a prayer to the ones up above
All the hate that you've heard has turned your spirit to a dove, oh ooh
Your spirit up above, oh ooh
I was choking in the crowd
Building my rain up in the cloud
Falling like ashes to the ground
Hoping my feelings, they would drown
But they never did, ever lived, ebbing and flowing
Inhibited, limited
'Til it broke up and it rained down
It rained down, like
You made me a, you made me a believer, believer
(Pain, pain)
You break me down, you built me up, believer, believer
(Pain)
I let the bullets fly, oh let them rain
My life, my love, my drive, it came from
(Pain)
You made me a, you made me a believer, believer
Last things last
By the grace of the fire and the flames
You're the face of the future, the blood in my veins, oh ooh
The blood in my veins, oh ooh
But they never did, ever lived, ebbing and flowing
Inhibited, limited
'Til it broke up and it rained down
It rained down, like
You made me a, you made me a believer, believer
(Pain, pain)
You break me down, you built me up, believer, believer
(Pain)
I let the bullets fly, oh let them rain
My life, my love, my drive, it came from
(Pain)
You made me a, you made me a believer, believer"""
    # print(sample)
    huffman = Huffman(sample)

    pprint.pprint(huffman.frequency_map)
    # pprint.pprint(huffman.huffman_tree)
    pprint.pprint(huffman.code_map)

    compressed_text = huffman.compress(sample)
    print(compressed_text)

    plain_text = huffman.decompress(compressed_text)
    print(plain_text)

