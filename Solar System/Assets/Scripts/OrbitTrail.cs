using UnityEngine;

[RequireComponent(typeof(LineRenderer))]
public class OrbitTrail : MonoBehaviour
{
    public float radius = 5f;
    public int segments = 100;

    void Start()
    {
        LineRenderer line = GetComponent<LineRenderer>();
        line.positionCount = segments + 1;
        line.useWorldSpace = false; // draws relative to this object's position (the Sun)
        line.loop = true;

        float angleStep = 360f / segments;

        for (int i = 0; i <= segments; i++)
        {
            float angle = Mathf.Deg2Rad * angleStep * i;
            float x = Mathf.Cos(angle) * radius;
            float z = Mathf.Sin(angle) * radius;
            line.SetPosition(i, new Vector3(x, 0f, z));
        }
    }
}