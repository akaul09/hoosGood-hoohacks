import React from 'react';
import './App.css';

// Updates the date
function App() {
  var today = new Date();
  var yyyy = today.getFullYear();
  var mm = today.getMonth();
  var dd = today.getDate();
  var day = new Array ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday",)
  var month = new Array ("January","February","March","April","May","June","July","August","September","October","November","December")
  var clock = dd + " " + month[mm] + " " + yyyy;
  return clock;
}
export default App;


// Poll 
// $(document).ready(function() {
//   var totalVotes = 0;
//   var data = {
//     p1: 0,
//     p2: 0,
//   };
  
//   updateDisplay(totalVotes, data);
  
//   $('button').on('click', function(evt) {
//     var btnClass = $(this).attr('class');
//     console.log('span.'+btnClass);
//     data[btnClass] += 1;
//     totalVotes += 1;
//     updateDisplay(totalVotes, data);
    
//     $('button').hide();
//   });
// });

// var updateDisplay = function(voteCount, data) {
//     for (var key in data) {
//     var sel = 'span.' + key;
//     $(sel).width(data[key] / voteCount * 100 + '%');
//     data[key] > 0 ? $(sel).html((data[key] / voteCount * 100).toFixed(0) + '%') : $(sel).html('0%');
      
//     $('#vote-count').html(voteCount + ' votes');
//   }
// };