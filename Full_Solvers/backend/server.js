const path = require('path');
const dotenv = require('dotenv');
const express = require('express');
const cors = require('cors');

const app = express();
dotenv.config();
app.use(cors());


let port = process.env.PORT || 3000;

// Routes
const nonogramRoutes = require('./routes/nonogram/nonogramRoutes');
const sudokuRoutes = require('./routes/sudoku/sudokuRoutes');

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use('/nonogram', nonogramRoutes);
app.use('/sudoku', sudokuRoutes);

// Serve frontend
if (process.env.NODE_ENV === 'production') {
    app.use(express.static(path.join(__dirname, '../frontend/build')));
  
    app.get('*', (req, res) =>
      res.sendFile(
        path.resolve(__dirname, '../', 'frontend', 'build', 'index.html')
      )
    );
  } else {
    app.get('/', (req, res) => res.send('Please set to production'));
  }
  

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
