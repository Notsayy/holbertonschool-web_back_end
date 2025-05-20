const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      try {
        const lines = data.split('\n').filter(line => line.trim() !== '');
        if (lines.length === 0) {
          console.log('Number of students: 0');
          resolve();
          return;
        }
        const header = lines[0].split(',');
        const fieldIndex = header.indexOf('field');
        const firstNameIndex = header.indexOf('firstname');
        const fields = {};
        let count = 0;
        for (let i = 1; i < lines.length; i++) {
          const line = lines[i].trim();
          if (line === '') continue;
          const values = line.split(',');
          if (values.length < header.length) continue;
          const field = values[fieldIndex];
          const firstname = values[firstNameIndex];
          if (!fields[field]) fields[field] = [];
          fields[field].push(firstname);
          count++;
        }
        console.log(`Number of students: ${count}`);
        for (const [field, names] of Object.entries(fields)) {
          console.log(
            `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`
          );
        }
        resolve();
      } catch {
        reject(new Error('Cannot load the database'));
      }
    });
  });
}

module.exports = countStudents;
