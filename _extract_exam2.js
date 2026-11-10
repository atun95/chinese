const fs = require('fs');
const h = fs.readFileSync('bai_test_hsk1.html', 'utf8');
const out = {};
for (const name of ['part1Data','part2Data','part3Data','part4Data','part5Data','part8Data']) {
  const start = h.indexOf('const ' + name + ' = [');
  if (start < 0) { console.log('MISS', name); continue; }
  const end = h.indexOf('\n    ];', start);
  const lit = h.slice(start + ('const ' + name + ' = ').length, end + 6);
  out[name] = eval('(' + lit + ')');
  console.log(name, out[name].length);
}
const pm = h.match(/const passageText = "([\s\S]*?)";/);
out.passageText = pm ? pm[1] : '';
fs.writeFileSync('lessons/hsk1_exam2_data.json', JSON.stringify(out, null, 1));
console.log('written');
