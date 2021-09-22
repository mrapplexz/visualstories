# VideoStories generation

# Part 1

## Text generation
```
cd image_generation
./install.sh
cd ..
python3 generate_text.py cuda:0 ./texts/text.txt 
```

# Part 2

## Frames generation
```
cd image_generation
./install.sh
cd ..
python3 generate_images.py ./texts/text.txt cuda:0,cuda:1 ./frames
```
