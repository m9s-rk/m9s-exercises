const testData = {
  reportCreated: new Date(),
  incomeShareAgreements: [
    {
      id: '1',
      name: 'Test Student 1',
      amount: 10000,
      createdAt: new Date('2021-02-15')
    },
    {
      id: '2',
      name: 'Test Student 2',
      amount: 12000,
      createdAt: new Date('2021-02-04'),
      contract: {
          signedAt: new Date('2021-02-07')
      }
    }
  ]
}

/**
 * Accepts an object of key:value pairs
 *
 * @param {Object} data - an object containing key:value pairs
 * @returns ???
 */
function mysteryFunction(data){
  const toReturn = { ...data }

  for (const key of Object.keys(data)){
    if (data[key] instanceof Date){
      toReturn[key] = data[key].toISOString()
    }
    else if (data[key] instanceof Array){
      toReturn[key] = data[key].map(value => mysteryFunction(value))
    }
    else if (typeof data[key] === 'object')  {
      toReturn[key] = mysteryFunction(data[key])
    }
  }

  return toReturn
}
