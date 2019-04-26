// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(X) {
    var isPositive = X >= 0
    var xString = Math.abs(X).toString()
    
    var split = xString.split("")
    
    var reversed = split.reverse()
    
    var parsed = parseInt(reversed.join(""))
    
    if(isPositive)
        return parsed
    else
        return parsed * -1
}