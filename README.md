# yuzu-keycap-hexcode-finder

nearestColor.py takes a hex color value and outputs the nearest five (or however many you specify) key color matches that Yuzu has to offer. You can also specify a specific keycap color name to test against the specified hexcode and see the distance between the two. The mapping was done by sampling every Yuzu example key image (using colorSampler.py) to obtain the average color value for each one, and then performing a simple distance check to find the most similar colors.

Yuzu provides a great service in creating custom keysets, but they don't list the hexcodes of their key colors. Conversly, they don't have as many key colors as there are hexcodes (obviously). I ran into a problem when using the keyboard drafting program [keyboard-layout-editor.com/] where I had designed a color palette that I was already in love with. When I tried to transfer this design to Yuzu, I couldn't find exact matches to my colors.

This program is currently written in python, and I plan to transition it to javascript so that I can have it run in github pages to be useful to the general masses. 

_Legal: I'm not (nor ever have been) associated with Yuzu. This code is has no warranty, I bear no liability._
