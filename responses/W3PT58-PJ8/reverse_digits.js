// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(x) {
    // write your code in JavaScript
    
    var multiples = [];
    
    for(i = 0; i < x; i++) {
        if(i % 3 == 0) {
            var alreadyContains = false;
            for(j = 0; j < multiples.length; j++) {
                if(multiples[j] == i) {
                    alreadyContains = true;
                    break;
                }
            }
            
            if(!alreadyContains) {
                multiples[multiples.length] = i;
            }
        }
        
        if(i % 5 == 0) {
            var alreadyContains = false;
            for(j = 0; j < multiples.length; j++) {
                if(multiples[j] == i) {
                    alreadyContains = true;
                    break;
                }
            }
            
            if(!alreadyContains) {
                multiples[multiples.length] = i;
            }
        }
    }
    
    var answer = 0;
    
    for(i = 0; i < multiples.length; i++) {
        answer += multiples[i];
    }
    
    return answer;
}