export default async function handler(req, res) {
  const { method, body } = req;
  console.log("Body: ", body)
  return res.sendStatus(201);
}
