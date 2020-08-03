 function myFunction() {

     //     Positive Points 

     var pScore0 = parseInt(document.getElementById('nAlphaUCBonus').innerHTML.replace(/^\D+/g, ''));
     var pScore1 = parseInt(document.getElementById('nAlphaLCBonus').innerHTML.replace(/^\D+/g, ''));
     var pScore2 = parseInt(document.getElementById('nNumberBonus').innerHTML.replace(/^\D+/g, ''));
     var pScore3 = parseInt(document.getElementById('nLengthBonus').innerHTML.replace(/^\D+/g, ''));
     var pScore4 = parseInt(document.getElementById('nSymbolBonus').innerHTML.replace(/^\D+/g, ''));
     var pScore5 = parseInt(document.getElementById('nMidCharBonus').innerHTML.replace(/^\D+/g, ''));
     var pScore6 = parseInt(document.getElementById('nRequirementsBonus').innerHTML.replace(/^\D+/g, ''));


     // Negative Points

     var nScore0 = parseInt(document.getElementById('nAlphasOnlyBonus').innerHTML.replace(/^\D+/g, ''));
     var nScore1 = parseInt(document.getElementById('nNumbersOnlyBonus').innerHTML.replace(/^\D+/g, ''));
     var nScore2 = parseInt(document.getElementById('nRepCharBonus').innerHTML.replace(/^\D+/g, ''));
     var nScore3 = parseInt(document.getElementById('nConsecAlphaUCBonus').innerHTML.replace(/^\D+/g, ''));
     var nScore4 = parseInt(document.getElementById('nConsecAlphaLCBonus').innerHTML.replace(/^\D+/g, ''));
     var nScore5 = parseInt(document.getElementById('nConsecNumberBonus').innerHTML.replace(/^\D+/g, ''));
     var nScore6 = parseInt(document.getElementById('nSeqAlphaBonus').innerHTML.replace(/^\D+/g, ''));
     var nScore7 = parseInt(document.getElementById('nSeqNumberBonus').innerHTML.replace(/^\D+/g, ''));
     var nScore8 = parseInt(document.getElementById('nSeqSymbolBonus').innerHTML.replace(/^\D+/g, ''));



     //     Total Point Calculation 

     var pTotal = pScore0 + pScore1 + pScore2 + pScore3 + pScore4 + pScore5 + pScore6;
     var nTotal = nScore0 + nScore1 + nScore2 + nScore3 + nScore4 + nScore5 + nScore6 + nScore7 + nScore8 ;
     var scoreTotal = pTotal - nTotal ;

     document.getElementById("result").innerHTML = scoreTotal;
 }
