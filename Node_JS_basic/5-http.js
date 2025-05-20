const http = require('http');
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
          resolve('Number of students: 0');
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
        let result = `Number of students: ${count}`;
        for (const [field, names] of Object.entries(fields)) {
          result += `\nNumber of students in ${field}: ${names.length}. List: ${names.join(', ')}`;
        }
        resolve(result);
      } catch {
        reject(new Error('Cannot load the database'));
      }
    });
  });
}

const database = process.argv[2];

const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    countStudents(database)
      .then((output) => {
        res.statusCode = 200;
        res.end(`This is the list of our students\n${output}`);
      })
      .catch(() => {
        res.statusCode = 200;
        res.end('This is the list of our students\nCannot load the database');
      });
  } else {
    res.statusCode = 404;
    res.end('Not found');
  }
});

app.listen(1245);

module.exports = app;