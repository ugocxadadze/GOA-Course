//1
function calculateAverage(grades) {
    const total = grades.reduce((acc, grade) => acc + grade, 0);
    return total / grades.length;
}


const grades = [8, 7, 9, 10, 6];
const average = calculateAverage(grades);

//2
function yearsUntil18(currentAge) {
    if (currentAge >= 18) {
        return 0; 
    }
    return 18 - currentAge;
}


const currentAge = 15; 
const yearsLeft = yearsUntil18(currentAge);

//3
function yearsUntil18(currentAge) {
    if (currentAge >= 18) {
        return 0; 
    }
    return 18 - currentAge;
}


const currentAge1 = 15; 
const yearsLeft1 = yearsUntil18(currentAge);
