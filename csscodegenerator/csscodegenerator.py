from PIL import Image
import glob

class CSSCodeGenerator:
    def __init__(self):
        print('starting program')
        generateTest()
        print('program succesfully exited')

def generateCode():
    print('generating code')

    template = '@keyframes {name} {from { background-position: 0px {sizeheight}px; } to { background-position: {sizewidth}px {sizeheight}px; }} .md [href="#{name}"] {display:inline-block;height: {height}px;width: {width}px; opacity: 1;vertical-align: middle;content: "";background: url(%%{filename}%%) {sizewidth}px {sizeheight}px no-repeat;animation: {name} {time}s steps({steps}) infinite;}'

    #result = template.replace('{name}', 'surprise')
    #TODO: name, sizewidth, delay, height, width, steps
    #width = 32, height = 32, delay = 0.1*f,

    image_folder = '/emoticons/'
    #image_path = image_folder + pcategory + '.png'
    #img = Image.open(image_path)

    emoticonsFileName = glob.glob('emoticons/*')

    result = ''

    filename = 'Dota2Emoticons5'

    counter = 0
    #abortcounter = 0

    for emoticonFileName in emoticonsFileName:
        name = emoticonFileName.replace('emoticons\\', '').replace('.png', '')
        width = 32
        img = Image.open(emoticonFileName)
        sizewidth, height = img.size
        steps = int(sizewidth/width)
        time = steps * 0.1

        partialResult = template
        partialResult = partialResult.replace('{name}', name)
        partialResult = partialResult.replace('{width}', str(width))
        partialResult = partialResult.replace('{height}', str(height))
        partialResult = partialResult.replace('{sizewidth}', '-' + str(sizewidth))
        partialResult = partialResult.replace('{steps}', str(steps))
        partialResult = partialResult.replace('{time}', str(time))
        partialResult = partialResult.replace('{filename}', filename)
        partialResult = partialResult.replace('{sizeheight}', '-' + str(height * counter))


        result = result + '\n\n' + partialResult

        counter += 1
        #abortcounter += 1
        #if abortcounter == 5: break


    print(result)


def generateImage():
    print('generating image')

    biggestSize = 0
    counter = 0
    #abortcounter = 0

    emoticonsFileName = glob.glob('emoticons/*')
    for emoticonFileName in emoticonsFileName:
        img = Image.open(emoticonFileName)
        size, height = img.size
        if size > biggestSize:
            biggestSize = size
        counter += 1

        #abortcounter += 1
        #if abortcounter == 5: break

    blank_image = Image.new("RGBA", (biggestSize, counter * 32))

    counter = 0
    #abortcounter = 0
    for emoticonFileName in emoticonsFileName:
        img = Image.open(emoticonFileName)

        blank_image.paste(img, (0, counter * 32))
        counter += 1


        #abortcounter += 1
        #if abortcounter == 5: break

    blank_image.save('ResultImage.png')

def generateTest():
    result = ''
    print('generating test comment')
    emoticonsFileName = glob.glob('emoticons/*')
    for emoticonFileName in emoticonsFileName:
        name = emoticonFileName.replace('emoticons\\', '').replace('.png', '')
        template = '[](#{name})`[](#{name})`  \n'
        result += template.format(name=name)

    print(result)

