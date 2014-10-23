import pyglet

image_frames=("an1.jpg","an2.jpg","an3.jpg","an4.jpg","an5.jpg","an6.jpg")


#about to create list of above images

images=map(lambda img:pyglet.image.load(img),image_frames)


#setting up display time of each image
#1.2 juss a random one
#animation total time will be 7.2 sec


animation=pyglet.image.Animation.from_image_sequence(images,0.5)

#creating sprite seq
animSprite=pyglet.sprite.Sprite(animation)

#main window with openGL context

w = animSprite.width
h = animSprite.height
win=pyglet.window.Window(width=w,height=h)

#bg color
pyglet.gl.glClearColor(1,1,1,1)


@win.event
def on_draw():
    win.clear()
    animSprite.draw()


pyglet.app.run()
