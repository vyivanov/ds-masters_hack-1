## ds-masters_hack-1

This is hackathon output (MISIS, SkillFactory, 19.10.20 - 24.10.20)

## what the target is?

Nowadays people all over the world wears different types of mask against COVID-19 situation.
Some of them are intended for protection function &ndash; we call them **OK**, but other are not &ndash; we call them **NG**.

![banner](src/banner.jpg)

So, we collected the bunch of mask examples and packed it to documented dataset to be used with ML algorithms.
It could be used in projects with raised requirements to types of mask.

Our work complements colleagues from France which created [synthetic dataset](https://github.com/cabani/MaskedFace-Net)
with correct and incorrect mask wearing. Combining of these two approaches to face masks recognition could bring even more value
in different CV projects.

Enjoy and wear right mask in right way!

## repository structure

```
|- src/             development scripts
|- data/            collected dataset
     |- kids/       photos of kids with OK and NG types of mask
         |- NG/
         |- OK/
     |- men/        photos of men with OK and NG types of mask
         |- NG/
         |- OK/
     |- women/      photos of women with OK and NG types of mask
         |- NG/
         |- OK/
|- spec.json        detailed specification of each photo
```

## specification description

```
"images": [ {   list of photos with meta data:
    " ## ":       1. sequence number of the photo
    "path":       2. relative path to photo
    "link":       3. link to original source
}, ... ]

```

## data collection methods

For this purpose we used ready [google.images scrapper](https://github.com/hardikvasa/google-images-download).
But there is a some problem with original code and it does not work out of the box. We found
[fix on issue tracker](https://github.com/hardikvasa/google-images-download/issues/331#issuecomment-710092724)
and successfully borrowed it.

In order to make things done we wrapped the scrapper to our scripts, grabbed images, manually marked the set and auto generated
specification via separate scripts.

## performance metrics

Existing image scrapper allowed us to grab **over 1500 photos** from google.images **in 30 minutes**. We have managed to filter
not appropriate photos and garbage in a **couple of hours**. Totally **\~25%** of grabbed images had been got to our dataset.

## further plans

- align photo formats: size, geometry, etc.
- balance amount of photos in OK and NG cases
- collect photos from other sources: [yandex.images](https://yandex.com/images/), [flickr](https://flickr.com/), etc.

## license agreement

You can freely use this content in educational and researching purposes.
