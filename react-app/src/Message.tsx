
function Message() {
    //JSX: Javascript XML
    const name = 'Chicken'
    if (name)
        return <h1>Hey {name}</h1>;
    return <h1>Hey Now</h1>
}

export default Message;