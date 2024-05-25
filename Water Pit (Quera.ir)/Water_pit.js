const height = [5, 2, 1, 3, 1, 4];
let totalWater = 0;

// Loop through each column from the second column to the second-to-last column.
for (let column = 1; column < height.length - 1; column++) {
    // Find the maximum height to the left of the current column.
    const maxLeft = Math.max(...height.slice(0, column));

    // Find the maximum height to the right of the current column.
    const maxRight = Math.max(...height.slice(column + 1));

    // Calculate the effective height of the current column (minimum of maxLeft and maxRight).
    const effHeight = Math.min(maxLeft, maxRight);

    // Calculate the amount of water that can be trapped in the current column.
    const waterColumn = effHeight - height[column];

    // Ensure waterColumn is greater than 0 before adding to totalWater.
    if (waterColumn > 0) {
        totalWater += waterColumn;
    }
}

// Print the total amount of trapped water.
console.log("Total trapped water:", totalWater);
