const customers = [
    {
        id:0,
        name: 'gerard'
    },
    {
        id:1,
        name: 'gerardinho'},
    {
        id:2,
        name: 'gerardote'},
    {
        id:3,
        name: 'gerardito'}
];

const invoices = [
    {
        customer_id: customers[0].id,
        amount: 123123,
        status: 'pending',
        date: '2026-11-03',
    },
    {
        customer_id: customers[1].id,
        amount: 123127,
        status: 'paid',
        date: '2026-11-04',
    },
    {
        customer_id: customers[2].id,
        amount: 123126,
        status: 'pending',
        date: '2026-11-04',
    },
    {
        customer_id: customers[3].id,
        amount: 123124,
        status: 'pending',
        date: '2026-11-06',
    }
];