const data = [
  { id: 1, name: 'John' },
  { id: 2, name: 'Jane' },
  { id: 3, name: 'Bob' },
];

const idToName = new Map(data.map((item) => [item.id, item]));

console.log('idToName :', idToName.size);

const foundName = idToName.get(2); // Returns "Jane"

console.log('foundName :', foundName);
