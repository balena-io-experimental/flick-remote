# GestuRemote

Adding gesture control to my ongoing smart home project using [resin.io](https://resin.io/), a flick hat and api
endpoints.

Resin.io recently received some free flick gear for Hack Friday, and I volunteered to take one for a test drive.
Using this I made an embedded remote control for my desk that interacts with another couple of projects (a lamp and a
rover, both API controlled).

[![video snapshot](/resources/video.png)](/resources/gesture_demo.mp4?raw=true)

## Hardware

* A multi-tool with knife and saw tooth bits.
* A pencil and small Phillips screwdriver.
* A raspberry pi (and microSD and USB power), flick hat and case.
* An Ikea desk (Pretty sure it's a Linnmon, but cannot guarantee it).
* Optional, some glue, but more on that later.

![Flick hat kit, multi-tool and pencil](/resources/materials.jpg)

### The Flick Hat (etc)

* The case and hat are well thought out and easy to assemble.
* The case can be assembled in two modes, and has push outs and suction cups to enable either.
	* It can be made into a sealed box unit, which is designed for stand-alone applications.
	* The upper surface can be spread out like wings for attaching to surfaces that you wish to gesture through.
* Oh, and of course it came with some neat stickers.

## Software

* resin.io of course!
	* This was always going to be an embedded gadget, so the obvious choice to make management easy was
	  resin.io.
	* It took me an hour or so to build up the docker template and file structure required, but now I've done that
	  work iteration is really easy.
* The [main source](/src/main.py) loads in the flick library, registers a couple of event handlers that fire http
  requests and advertises all this on the console.
* Oh, and of course it came with a neat unicorn.

## Install

* Draw round the case (An improvement would be to cut at a slightly jaunty angle, for push and twist).
* Cut the lower surface of the desk, and pull out a bunch of the hexagon paper filler.
* Glue the wings of the case to the upper surface of the desk (or, use a push and twist install if you follow my
  improved method). ![Flick hat embedded into desk](/resources/lower_view.jpg)
* [Sketch out the active area](/resources/upper_view_test.jpg) on the upper surface, and test.
* Mark the active area, so it's nice an easy to landmark your gestures.

## Result

* The case came with a neat sticker; but the rest of my office is Star Wars themed, so of course I custom printed my
  own decal. ![rebel logo on desk](/resources/upper_view_final.jpg)
* A controller isn't much good without anything to control, so I took a rover I built and lamp I've retro-fitted, and
  pointed the gestures to their endpoints.
  [![video snapshot](/resources/video.png)](/resources/gesture_demo.mp4?raw=true)

## Improvements

* Cut the desk at a slight angle to your final install orientation.  The box is almost exactly the same height as the
  void in the desk, so a push and twist install, without the wings, would be easy.
* Make a PiBow style layered case for the gadget, they are much sturdier.
