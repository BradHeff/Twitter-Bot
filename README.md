<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/BradHeff/Twitter-Bot">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Twitter Bot - Python</h3>

  <p align="center">
    A Twitter Bot built with Python utilizing GPT2
    <br />
    <a href="https://github.com/BradHeff/Twitter-Bot"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/bradheff/Twitter-Bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/bradheff/Twitter-Bot/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#todo">TODO:</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://www.horizon.sa.edu.au)-->

This repository holds the code for creating a simple twitter bot using GPT2. All current code is located in deepproverbs.py.<br/>


### TODO
Build the model and push to huggingface

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python3]][python-url]
* [![GPT2][GPT2]][GPT2-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

Software needed for this application to work
* python 3.8
* * Windows: 
* * * [Download Python](python-url)
* * Linux:
* * *  ```sudo apt install python3```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/bradheff/Twitter-Bot.git
   ```

### Setting Up Environment

The associated Makefile should make playing with the code simple. 
*To start:*
* run either a jupyter or terminal environment with `make run-jupyter` or `make run`

That's all you need to start playing around with the code.

If you've trained a model and want to tweet something you can run 
```
make CHECKPOINT_DIR="deepproverbs" TWITTER_CREDS="twitter.json" tweet
```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Nothing to show as of yet.

_For more examples, please refer to the [Documentation](https://github.com/BradHeff/Twitter-Bot/wiki)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/bradheff/Twitter-Bot/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@bradheffernan](https://twitter.com/bradheffernan) - brad.heffernan83@outlook.com

Project Link: [https://github.com/bradheff/Twitter-Bot](https://github.com/bradheff/Twitter-Bot)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [nbertagnolli](https://github.com/nbertagnolli/DeepProverbs)
* * Cloned and altered from his/her github `DeepProverbs` Thanks for the starter kit.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/bradheff/Twitter-Bot.svg?style=for-the-badge
[contributors-url]: https://github.com/bradheff/Twitter-Bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/bradheff/Twitter-Bot.svg?style=for-the-badge
[forks-url]: https://github.com/bradheff/Twitter-Bot/network/members
[stars-shield]: https://img.shields.io/github/stars/bradheff/Twitter-Bot.svg?style=for-the-badge
[stars-url]: https://github.com/bradheff/Twitter-Bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/bradheff/Twitter-Bot.svg?style=for-the-badge
[issues-url]: https://github.com/bradheff/Twitter-Bot/issues
[license-shield]: https://img.shields.io/github/license/bradheff/Twitter-Bot?style=for-the-badge
[license-url]: https://github.com/BradHeff/Twitter-Bot/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/brad-heffernan83/

[product-screenshot]: images/screenshot1.png

[Python3]: https://img.shields.io/badge/Python-35495E?style=for-the-badge&logo=python&logoColor=61DAFB
[GPT2]: https://img.shields.io/badge/GPT2-FFA500?style=for-the-badge&logo=openai&logoColor=000000
[GPT2-url]: https://openai.com/
[python-url]: https://www.python.org/
