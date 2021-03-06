from discord.ext import commands


@commands.command()
async def mc(ctx, *, arg):
    CODE = {
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ' ': '/',
        '.': '.-.-.-',
        ',': '--..--',
        '?': '..--..',
        "'": '.----.',
        '"': ".-..-.",
        '!': '-.-.--',
        '@': '.--.-.',
        '$': '...-..-',
        ":": "---...",
        ";": "-.-.-.",
        "=": "-...-",
        '-': '-....-',
        '+': '.-.-.',
        '/': '-..-.',
        '&': '.-...'
    }

    z = str(arg)
    z = z.lower()
    signs = ["՜", "#", "%", "^", "*", "(", ")", "-", '"']
    for i in range(0, len(signs)):
        x = signs[i]
        z = z.replace(x, "")
    printer = ""

    for j in z:
        for i in CODE.items():
            if (j == i[0]):
                printer = printer + ' ' + i[1]

    await ctx.send(printer)


def setup(client):
    # Every extension should have this function
    client.add_command(mc)
