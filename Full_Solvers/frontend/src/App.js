import {Route, BrowserRouter as Router, Routes } from 'react-router-dom';
import Nonogram from "./components/Nonogram";
import Sudoku from "./components/Sudoku";
import NonogramSplash from './components/NonogramSplash';
import SudokuSplash from './components/SudokuSplash';
import Congratulations from './components/Congratulations';
import Header from './components/Header';
import Home from './components/Home';

function App() {
  return (
    <div className="App">
      <Router>
        <Header />
        <div className='container'>
          <Routes>
            <Route path='/' element={<Home />} />
            <Route path='/nonogram-game' element={<NonogramSplash />} />
            <Route path='/nonogram-game/:size' element={<Nonogram />} />
            <Route path='/sudoku-game' element={<SudokuSplash />} />
            <Route path='/sudoku-game/:difficulty' element={<Sudoku />} />
            <Route path='/victory/:game' element={<Congratulations />} />
          </Routes>
        </div>
      
      </Router>
    </div>
  );
}

export default App;
