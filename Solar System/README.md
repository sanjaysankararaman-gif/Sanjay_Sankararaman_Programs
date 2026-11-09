# Solar System (VR)

An interactive, immersive Solar System built in Unity for VR. The aim is to let the user move through a scaled, animated model of the Solar System and look closely at the planets, moons and other objects. **Status: in progress.**

## Features so far

- Planets orbiting the Sun, driven by an orbit script
- Moons, using 3D models of Earth's Moon, Phobos, Deimos, Europa, Io, Titan-class moons and others
- Saturn with a ring system
- An asteroid belt generated from a set of asteroid models
- A comet with an orbit and a trail
- Orbit trails showing each body's path
- A starfield skybox and a generated galaxy backdrop
- Keyboard camera movement for testing outside a headset
- VR support through the XR Interaction Toolkit, with an XR Device Simulator for testing without a headset

## Tech Used

- **Unity** with the Universal Render Pipeline (URP)
- **C#** for orbits, trails, the asteroid belt, Saturn's rings and the camera
- **XR Interaction Toolkit** and **OpenXR** for VR
- Texture maps and 3D models of the planets and moons

## Project Structure

- `Assets/Scripts` — orbit, comet, asteroid belt, ring and camera scripts
- `Assets/Scenes/SolarSystem.unity` — the main scene
- `Assets/Textures` and `Assets/Moons_gIb` — planet textures and moon models

## What I'm Working On Next

I am working on adding a walkthrough feature as an educational feature for kids.

