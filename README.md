# VideoStories generation

# Part 2

## Frames generation
```
cd image_generation
./install.sh
cd ..
python3 generate_images ./texts/text.txt cuda:0,cuda:1 ./frames
```
