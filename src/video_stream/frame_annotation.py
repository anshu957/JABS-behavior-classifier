import cv2
from shapely.geometry import MultiPoint

_FRAME_LABEL_COLOR = (215, 222, 0)


def label_identity(img, pose_est, identity, frame_index,
                   color=_FRAME_LABEL_COLOR):
    """
    label the identity on an image
    :param img: image to label
    :param pose_est: pose estimations for this video
    :param identity: identity to label
    :param frame_index: index of frame to label
    :param color: color to use for label
    :return: None
    """

    shape = pose_est.get_identity_convex_hulls(identity)[frame_index]

    if shape is not None:
        center = shape.centroid

        # draw a marker at this location. this is a filled in circle and then
        # a larger unfilled circle
        cv2.circle(img, (int(center.y), int(center.x)), 3, color,
                   -1, lineType=cv2.LINE_AA)
        cv2.circle(img, (int(center.y), int(center.x)), 6, color,
                   1, lineType=cv2.LINE_AA)


def label_all_identities(img, pose_est, identities, frame_index):
    """
    label all of the identities in the frame
    :param img: image to draw the labels on
    :param pose_est: pose estimations for this video
    :param identities: list of identity names
    :param frame_index: index of frame, used to get all poses for frame
    :return: None
    """

    for identity in identities:
        shape = pose_est.get_identity_convex_hulls(identity)[frame_index]
        if shape is not None:
            center = shape.centroid

            # write the identity at that location
            cv2.putText(img, str(identity), (int(center.y), int(center.x)),
                        cv2.FONT_HERSHEY_PLAIN, 1, _FRAME_LABEL_COLOR, 1,
                        lineType=cv2.LINE_AA)
