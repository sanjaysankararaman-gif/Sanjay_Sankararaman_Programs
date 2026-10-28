using UnityEngine;

[RequireComponent(typeof(MeshFilter), typeof(MeshRenderer))]
public class RingMeshGenerator : MonoBehaviour
{
    public float innerRadius = 1.2f;
    public float outerRadius = 2.2f;
    public int segments = 128;

    void Start()
    {
        Mesh mesh = new Mesh();
        Vector3[] vertices = new Vector3[(segments + 1) * 2];
        Vector2[] uvs = new Vector2[vertices.Length];
        int[] triangles = new int[segments * 6];

        for (int i = 0; i <= segments; i++)
        {
            float angle = (float)i / segments * Mathf.PI * 2f;
            float x = Mathf.Cos(angle);
            float z = Mathf.Sin(angle);

            vertices[i * 2] = new Vector3(x * innerRadius, 0, z * innerRadius);
            vertices[i * 2 + 1] = new Vector3(x * outerRadius, 0, z * outerRadius);

            // UV.x = 0 at inner edge, 1 at outer edge — this drives the radial texture wrap
            uvs[i * 2] = new Vector2(0, (float)i / segments);
            uvs[i * 2 + 1] = new Vector2(1, (float)i / segments);
        }

        for (int i = 0; i < segments; i++)
        {
            int idx = i * 6;
            int v = i * 2;

            triangles[idx] = v;
            triangles[idx + 1] = v + 1;
            triangles[idx + 2] = v + 2;

            triangles[idx + 3] = v + 1;
            triangles[idx + 4] = v + 3;
            triangles[idx + 5] = v + 2;
        }

        mesh.vertices = vertices;
        mesh.uv = uvs;
        mesh.triangles = triangles;
        mesh.RecalculateNormals();

        GetComponent<MeshFilter>().mesh = mesh;
    }
}