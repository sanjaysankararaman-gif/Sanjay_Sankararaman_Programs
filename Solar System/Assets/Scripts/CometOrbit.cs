using UnityEngine;

public class CometOrbit : MonoBehaviour
{
    public Transform sun;
    public float semiMajorAxis = 34f;
    public float semiMinorAxis = 20f;
    public float orbitSpeed = 20f;
    public float spinSpeed = 15f;
    public float startAngle = 0f;   // NEW — lets each comet begin at a different point in its orbit

    private float angle;

    void Start()
    {
        angle = startAngle;   // NEW — initialize from the Inspector value instead of always 0
    }

    void Update()
    {
        angle += orbitSpeed * Time.deltaTime;
        float rad = angle * Mathf.Deg2Rad;

        float x = Mathf.Cos(rad) * semiMajorAxis;
        float z = Mathf.Sin(rad) * semiMinorAxis;

        float focusOffset = Mathf.Sqrt(semiMajorAxis * semiMajorAxis - semiMinorAxis * semiMinorAxis);

        transform.position = sun.position + new Vector3(x - focusOffset, 0, z);

        transform.Rotate(Vector3.up, spinSpeed * Time.deltaTime, Space.Self);
    }
}