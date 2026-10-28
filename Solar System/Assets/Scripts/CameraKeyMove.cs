using UnityEngine;
using UnityEngine.InputSystem;

public class CameraKeyMove : MonoBehaviour
{
    public float moveSpeed = 10f;

    void Update()
    {
        Keyboard kb = Keyboard.current;
        if (kb == null) return;

        float forward = 0f;
        float side = 0f;
        if (kb.upArrowKey.isPressed)    forward += 1f;
        if (kb.downArrowKey.isPressed)  forward -= 1f;
        if (kb.rightArrowKey.isPressed) side += 1f;
        if (kb.leftArrowKey.isPressed)  side -= 1f;

        Vector3 move = (transform.forward * forward + transform.right * side) * moveSpeed * Time.deltaTime;
        transform.position += move;
    }
}