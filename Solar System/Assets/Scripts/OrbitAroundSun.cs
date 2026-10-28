using UnityEngine;

public class OrbitAroundSun : MonoBehaviour
{
    public Transform sun;          // drag the Sun object here in Inspector
    public float orbitSpeed = 20f; // degrees per second around the sun
    public float spinSpeed = 50f;  // degrees per second on its own axis

    void Update()
    {
        // Orbit: rotate this planet around the sun's position, on the Y axis
        transform.RotateAround(sun.position, Vector3.up, orbitSpeed * Time.deltaTime);

        // Spin: rotate the planet on its own local Y axis
        transform.Rotate(Vector3.up, spinSpeed * Time.deltaTime, Space.Self);
    }
}