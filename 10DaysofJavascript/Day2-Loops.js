'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    let vowel = [];
    let vowels = ["a", "e", "i", "o", "u"];
    let consoants = [];
    for(let letter of s.split('')){
        if(vowels.indexOf(letter.toLowerCase()) !== -1){
            vowel.push(letter);
        }else{
            consoants.push(letter);
        }
    }

    for(let letter of vowel){
        console.log(letter);
    }

    for(let letter of consoants){
        console.log(letter);
    }
}


function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}
