//filling the puzzle
//refer to the link on hackerranck https://www.hackerrank.com/challenges/crossword-puzzle/problem

'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function transposeCrossword(crossword) {
    var transposedCrossword = new Array(10).fill(0)

    for (var i in transposedCrossword) {
        transposedCrossword[i] = new Array(10).fill(0)
    }

    for (var i in crossword) {
        for (var j in crossword[i]) {
            transposedCrossword[i][j] = crossword[j][i]
        }
    }
    transposedCrossword = transposedCrossword.map(x => x.join(""))
    return transposedCrossword;
}

function findFillPostion(crossword, length, transposeCrossword, word) {
    var position = [];
    let regstr = ""
    for (let i of word) {
        regstr += `[${i}-]`
    }
    regstr += "-*"
    var reg = new RegExp(regstr)
    for (var i in crossword) {
        var tempPattern = crossword[i].match(reg)
        if (tempPattern && tempPattern[0].length == word.length) {
            position.push([Number(i), crossword[i].indexOf(tempPattern), 'h'])
        }
    }
    for (var i in transposeCrossword) {
        var tempPattern = transposeCrossword[i].match(reg)
        if (tempPattern && tempPattern[0].length == word.length) {
            position.push([transposeCrossword[i].indexOf(tempPattern) ,Number(i), 'v'])
        }
    }

    return position;
}

function fillPuzzle(crossword, word, location) {
    crossword[location[0]] = crossword[location[0]].split("");
    
    word = word.split("");
    crossword[location[0]].splice(location[1], word.length, ...word)
    crossword[location[0]] = crossword[location[0]].join("");
    return crossword;
}

// Complete the crosswordPuzzle function below.
function crosswordPuzzle(crossword, hints) {
    hints = hints.split(";");

    return _crosswordPuzzle(crossword, hints)
}

function _crosswordPuzzle(crossword, hints) {
    let originalCrossWord = Array.from(crossword)
    if (hints.length == 0 && crossword.every(x => !x.includes("-"))) {
        return crossword;
    }

    for (let i of hints) {
        let transposeCW = transposeCrossword(crossword);
        let positions = findFillPostion(crossword, i.length, transposeCW, i);
        for (let j of positions) {
            if (j[2] == 'h') {
                crossword = fillPuzzle(crossword, i, j)
            }
            else if (j[2] == 'v') {
                crossword = transposeCrossword(crossword)
                crossword = fillPuzzle(crossword, i, [j[1], j[0], j[2]])
                crossword = transposeCrossword(crossword)
            }
            var tempHint = Array.from(hints)
            tempHint.splice(tempHint.indexOf(i), 1)
            
            let result = _crosswordPuzzle(crossword, tempHint);
            crossword = originalCrossWord
            if (result) {
                return result;
            }
        }
    }
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    let crossword = [];

    for (let i = 0; i < 10; i++) {
        const crosswordItem = readLine();
        crossword.push(crosswordItem);
    }

    const words = readLine();

    const result = crosswordPuzzle(crossword, words);

    ws.write(result.join('\n') + '\n');

    ws.end();
}
