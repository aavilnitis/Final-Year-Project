const express = require('express');
const router = express.Router();
const { solveGame, getAllGames, getSmallGames, getMediumGames, getLargeGames, getXlGames} = require('../../controllers/nonogram/nonogramController')


router.get('/', getAllGames)
router.get('/small', getSmallGames);
router.get('/medium', getMediumGames);
router.get('/large', getLargeGames);
router.get('/xl', getXlGames);
router.post('/solve', solveGame);

module.exports = router;