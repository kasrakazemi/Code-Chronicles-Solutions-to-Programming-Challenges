// Define the wheel and password
const wheel = "RTIGFIPR";
const password = "GFI";

// Function to find all occurrences of a character in the wheel
function findLetters(character) {
  const outputList = [];
  for (let index = 0; index < wheel.length; index++) {
    if (character === wheel[index]) {
      outputList.push([index, wheel[index]]);
    }
  }
  return outputList;
}

// Function to find the shortest distance from the pointer to a character
function findDistance(pointer, letters) {
  const minimums = [];

  for (const i of letters) {
    const startPoint = pointer;
    const endPoint = i[0];
    const clockwise = (endPoint - startPoint + wheel.length) % wheel.length;
    const antiClockwise = (startPoint - endPoint + wheel.length) % wheel.length;
    minimums.push([i[0], Math.min(clockwise, antiClockwise)]);
  }

  const [outputIndex, outputValue] = minimums.reduce((min, curr) =>
    curr[1] < min[1] ? curr : min
  );

  return [outputIndex, outputValue];
}

let pointer = 0; // Initial pointer position
let totalRotations = 0; // Total rotations needed to reach the characters
let totalTime = 0; // Total time taken to reach the characters

// Iterate through each character in the password
for (const char of password) {
  const letters = findLetters(char);
  const [closestLetter, rotations] = findDistance(pointer, letters);
  pointer = closestLetter; // Update the pointer position
  totalRotations += rotations;
  totalTime += 1;
}

// Print the total duration (time + rotations) to reach all password characters
console.log('Total Duration: ', totalTime + totalRotations, 's');
