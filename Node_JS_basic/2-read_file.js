const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.trim().split('\n');
    const students = lines.slice(1).filter(line => line.trim() !== '');
    console.log(`Number of students: ${students.length}`);

    const fields = {};
    students.forEach(line => {
      const parts = line.split(',');
      const firstname = parts[0];
      const field = parts[parts.length - 1];
      if (!fields[field]) fields[field] = [];
      fields[field].push(firstname);
    });

    for (const field in fields) {
      console.log(
        `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`
      );
    }
  } catch {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
