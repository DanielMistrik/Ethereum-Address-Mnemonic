// Used with browserify to access a keccak hashing library
var keccak256 = require('keccak256')
global.window.keccak256 = keccak256