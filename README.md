# AI Music Generation

This project aims to fuse 2 tracks of music together, using two methods. A Variational Auto Encoder and a Generative Adversarial Network.
Included in this project are also:
* A website which showcases some examples as well as serves as an interface for both systems.
* A site scraper which was used to efficiently download midi samples from websites which offer them.
* A transposer which chages all midi file samples to the same key.



## Description

Three approaches were taken to achieve this task:
1. Interpolation on Existing Music
    Passing 2 MIDI tracks through a Variational AutoEncoder.
2. GAN given all of the Music as a Training Set
    A MIDI Track produced by a Generative Adversarial Network trained on a particular Training Set.
3. New Music produced by GAN then interpolated by VAE
    Passing the 2 MIDI tracks produced by the Generative Adversarial Network through the Variational AutoEncoder.

## Getting Started

### Dependencies

* Python 3.8.8

* Flask version 1.1.2
* note_seq version 0.0.3
* magenta version 2.1.3
* Keras version 2.4.3
* Jinja2 version 2.11.3
* music21 version 6.7.1
* matplotlib version 3.4.1
* numpy version 1.19.5


### Installing

To install all above libraries at one go
```
pip install -r requirements.txt
```


### Executing program

* Open a terminal
* cd to current directory
* Run the following command
```
python -m flask run
```
* Open link given

<!-- 
## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```
 -->
## Authors

Contributors names and contact info

* Paolo Bezzina - [@PaoloBezzina](https://github.com/PaoloBezzina)
* Logan Formosa - [@lowgunnn](https://github.com/lowgunnn)
* Yran Riahi - [@YranRiahi](https://gitlab.com/YranRiahi)
* David Dimech - [@daviddimec](https://gitlab.com/daviddimech)
* Daniel Grech - [@dangee303](https://gitlab.com/dangee303)

<!-- 
## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details
 -->

## Acknowledgments

* [Music-VAE](https://magenta.tensorflow.org/music-vae)
* [Magenta](https://magenta.tensorflow.org)
* [OpenAi Jukebox](https://openai.com/blog/jukebox/)
* [Rave Dj](https://rave.dj/mix)
