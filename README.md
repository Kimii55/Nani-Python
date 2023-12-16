# Nani API - Library
Simple API requests with many output customizations, access to over 1k images with a token-protected system.

### Why should I use this library?
So that you have fewer problems using the API and so that you also have to use less code, we have decided to program a library to make it easier for developers.

### An example of the use of the library
```py
import naniapi

nani = naniapi.NaniAPI("token")

await nani.gif("kiss")
await nani.get("gif", "kiss")
await nani.random("gif")
await nani.endpoints("gif")

stats = await nani.stats()
```
