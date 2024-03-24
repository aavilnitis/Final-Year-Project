const express = require('express');
const router = express.Router();
const { getEasyGame, getMediumGame, getHardGame, solveGame } = require('../../controllers/sudoku/sudokuController')


router.get('/easy', getEasyGame)
router.get('/medium', getMediumGame)
router.get('/hard', getHardGame)
router.post('/solve', solveGame)

module.exports = router;