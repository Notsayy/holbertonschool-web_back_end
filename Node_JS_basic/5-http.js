const http = require('http');
const fs = require('fs').promises;

const app = http.createServer(async (req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    try {
      const database = process.argv[2];
      if (!database) {
        throw new Error('Database file not provided');
      }

      const data = await fs.readFile(database, 'utf8');
      const lines = data.split('\n').filter((line) => line.trim() !== '');

      if (lines.length <= 1) {
        res.statusCode = 200;
        res.end('This is the list of our students\nNumber of students: 0');
        return;
      }

      const students = [];
      const fields = {};

      for (let i = 1; i < lines.length; i++) {
        if (lines[i].trim() === '') continue;

        const [firstname, , , field] = lines[i].split(',');
        if (!firstname || !field) continue;

        students.push({ firstname, field });

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      }

      let response = 'This is the list of our students\n';
      response += `Number of students: ${students.length}\n`;

      for (const [field, names] of Object.entries(fields)) {
        response += `Number of students in ${field}: ${
          names.length
        }. List: ${names.join(', ')}\n`;
      }

      res.statusCode = 200;
      res.end(response.trim());
    } catch (error) {
      res.statusCode = 500;
      res.end(`This is the list of our students\n${error.message}`);
    }
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

app.listen(1245, () => {
  console.log('Server running at http://localhost:1245/');
});

module.exports = app;
