/**
 * Returns the sum of all integers in the comma delimited string.
 * 
 * NOTE: I'm not handling integer overflow or underflow. In a perfect world, I would perform 
 * the addition using strings. I don't think this will overflow or underflow though.  
 * 
 * @param {*} S Comma delimited string of 32-bit integers, returns their sum.
 */
function solution(S) {
  const input = `${S}`
  const arr = input.split(/,\s*/);

  return arr.reduce((sum, current) => {
    const currentInt = Number(current);
    if (!Number.isInteger(currentInt)) {
      throw new Exception("Invalid Value!");
    }

    return sum + Number(current);
  }, 0);
}