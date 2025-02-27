import Link from "next/link";

export default function ProjectDetailsLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <>
            {children}
            <h3>
                <Link href="./"
                className="text-blue-500 mr-4">Back to projects</Link>
            </h3>
        </>
    )
}