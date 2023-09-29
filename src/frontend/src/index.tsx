import React from 'react';
import ReactDOM from 'react-dom';
import { Table, Container } from 'reactstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import * as faker from 'faker';

const generateFakeRows = (count: number) => {
  const rows = [];
  for (let i = 0; i < count; i++) {
    rows.push({
      id: i + 1,
      name: faker.name.findName(),
      email: faker.internet.email(),
      company: faker.company.companyName(),
      city: faker.address.city(),
    });
  }
  return rows;
};

const App: React.FC = () => {
  const rows = generateFakeRows(10);

  return (
    <Container className="mt-5">
      <Table hover responsive bordered>
        <thead>
          <tr>
            <th>#</th>
            <th>Name</th>
            <th>Email</th>
            <th>Company</th>
            <th>City</th>
          </tr>
        </thead>
        <tbody>
          {rows.map(row => (
            <tr key={row.id}>
              <th scope="row">{row.id}</th>
              <td>{row.name}</td>
              <td>{row.email}</td>
              <td>{row.company}</td>
              <td>{row.city}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Container>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));

