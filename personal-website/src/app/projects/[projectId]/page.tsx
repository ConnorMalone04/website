export default async function First({
    params,
}: {
    params: Promise<{ projectId: string }>;
}) {
    const projectId = (await params).projectId;
    return <h1>Details about project {projectId}</h1>;
}