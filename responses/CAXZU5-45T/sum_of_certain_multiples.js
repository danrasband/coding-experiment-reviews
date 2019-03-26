function solution(x) {
  if (!Number.isInteger(Number(x))) {
    return null;
  }

  const values = [];
  let sum = 0;

  let subject = x - 1;
  while (subject > 0) {
    if (subject % 3 && subject % 5) {
      subject = subject - 1;
      continue;
    } else if (subject % 3 || subject % 5) {
      sum += subject;
      values.push(subject);
    }

    subject = subject - 1;
  }

  if (values.length === 0) {
    return null;
  }

  return sum;
}
