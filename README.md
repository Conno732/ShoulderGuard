# ShoulderGuard
 A chrome extension that prevents shoulder surfers from peaking at your screen in public using a face recognition system.

## Note: 
Facial recognition --> main branch

Server code --> server-testing branch

The chrome extension --> chrome-extension branch

There is another alert-page branch that is unused in favor of an on-website popup


# Demo
https://www.youtube.com/watch?v=MWtmmSZ56kg&ab_channel=ConnorWalters


# How to use:

Clone the repo, switch to the chrome-extension branch, and then set the repo as an unpacked chrome extension.

To set it as an unpacked chrome extension, go to extensions > manage extensions > enable developer mode.

Select "load unpacked" and then select the cloned repo.



## Inspiration
Shoulder surfing, as the name implies, occurs when an attacker tries to look directly over someone's shoulder to obtain PIN, passwords, or other sensitive information. A recent study found that 73% of survey respondents indicated they had seen someone else’s confidential PIN without them knowing. Due to the massive presence and potential security risks that come from shoulder surfing, our team decided to combat this problem

## What it does
We created a chrome extension app that uses a facial recognition algorithm (HOG) to determine whether there is another person looking over the screen during the moment when the user is entering their passwords. In a case when shoulder surfing is detected, the app automatically notifies the user via a popup window. Our app does not store any information from the user and only activates the laptop's camera when a password field is interacted with.

## How we built it
We used a google chrome extension to host the majority of our code. It tracks if the user is trying to type in sensitive information by using event listeners, and will use the camera to take a picture of the user when these events are triggered. After taking the picture we needed a way to recognize if there was multiple faces in the picture. We chose to upload the picture to a webserver and run the algorithm there, and return an answer. To do this we had the JavaScript in our extension perform an XMLHTTP request and upload the image for an answer. To host the webserver we used Heroku, and implemented a python webserver using the Flask framework. By doing this we were able to accept POST requests from the chrome extension to upload images. Once the Flask server has parsed the image from the request, it uses a machine learning library that implements a face detection algorithm. After the algorithm detects the amount of faces, we had it respond with an answer.  We programmed the extension to produce a popup in the case where the algorithm finds more than one face, meaning the user is being watched.

## Challenges we ran into
We had a lot of trouble with getting all of the libraries and dependencies to play nice with our web server. This was further complicated by the fact that we never even programmed a web server before! We had to force ourselves to learn the Flask framework and how to deploy to Heroku server in the span of 12 hours. This took a lot of effort for us, and was probably our biggest challenge. Learning networking plus all of the webserver technology took up a lot of our time, but in the end we were able to produce a viable product.

## Accomplishments that we're proud of
We are really proud of our idea, and our brainstorming process. Tackling the machine learning challenge makes it hard to make products that can have a potential impact in the real world. We found a lot of machine learning projects are somewhat inaccessible due to the highly technical features they have, while our product is designed to be simple and accessible.

We are also proud of how much we learned along the way. Being able to get a new understanding of networking was a fun experience. The amount we learned in such a short period was pretty impressive to us.

## What we learned
We had to do a decent bit of research on how networking and webservers work. Beforehand we were both unsure what Get and Post requests were, but now we feel like we have a solid understanding on how those things work. We also learned a lot on how machine learning and algorithms can be used to detect faces. Finally, we learned how chrome extensions work, and how to make one of our own.

## What's next for ShoulderGuard
Continuing the ShoulderGuard project, we feel like there are a lot of features we could add. One such feature would be the ability to increase the amount of faces that would trigger a popup. We also thought of using facial recognition so that we could make the algorithm ignore any familiar faces while blocking any unfamiliar faces. We would also be interested in trying to have ShoulderGuard use an algorithm that can detect external cameras as well, further preventing shoulder surfing.

If we wanted to turn ShoulderGuard into a real world product, we would want it to be a product for businesses. With the prevalence of remote work, companies are giving employees the choice to work anywhere. This would only increase the amount of opportunities for shoulder surfers. Having ShoulderGuard installed on all company issued laptops would prevent attackers from being able to target companies through shoulder surfing. 
