Redis - Remote Dicitionary server

Use case: message broker (pub/sub methods), web page visit count, Web page cookies storage

similar to mysql, db is there. default value is 0 during login. It can be changed.

list, hash (key, field,value,f,v,f,v...), strings, set

for each key, expiry timer can be set

for each value, expiry timer can be set

Redis cli acts as client to Redis server

Lua interpreter is used for Redis scripting

Redis client if required can use AUTH for accessing Redis server

Many subscriber & many publisher is possible
