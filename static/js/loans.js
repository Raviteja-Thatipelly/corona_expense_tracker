const loans = [
    { id: 1, amount: 50000, status: 'Ongoing', emi: [5000, 5000, 5000] },
    { id: 2, amount: 30000, status: 'Completed', emi: [3000, 3000, 3000] },
    { id: 3, amount: 70000, status: 'Ongoing', emi: [7000, 7000, 7000] },
  ];
  
  function updateSummary() {
    document.getElementById('totalLoans').textContent = `Total Loans: ${loans.length}`;
    document.getElementById('completedLoans').textContent = `Completed: ${loans.filter(l => l.status === 'Completed').length}`;
    document.getElementById('ongoingLoans').textContent = `Ongoing: ${loans.filter(l => l.status === 'Ongoing').length}`;
  }
  
  function loadLoans() {
    const tbody = document.querySelector('#loanTable tbody');
    tbody.innerHTML = '';
  
    loans.forEach(loan => {
      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td>${loan.id}</td>
        <td>₹${loan.amount}</td>
        <td>${loan.status}</td>
        <td><button onclick="viewEMI(${loan.id})">View EMI</button></td>
      `;
      tbody.appendChild(tr);
    });
  }
  
  function viewEMI(id) {
    const loan = loans.find(l => l.id === id);
    const emiHTML = loan.emi.map((e, i) => `<li>EMI ${i + 1}: ₹${e}</li>`).join('');
    document.getElementById('emiSection').innerHTML = `<ul>${emiHTML}</ul>`;
  }
  
  updateSummary();
  loadLoans();
  